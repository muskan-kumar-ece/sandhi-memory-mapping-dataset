#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def iter_paths(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        yield path


def human_bytes(size: int) -> str:
    value = float(size)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if value < 1024 or unit == "TB":
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} TB"


def safe_read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compute_records_and_tokens(
    json_files: List[Path],
) -> Tuple[int, Dict[str, int], Optional[int], str, int]:
    record_total = 0
    record_counts_by_type: Dict[str, int] = {}
    token_total: Optional[int] = None
    token_method = "unavailable"
    parse_failures = 0

    tokenizer = None
    try:
        import tiktoken  # type: ignore

        tokenizer = tiktoken.get_encoding("cl100k_base")
        token_total = 0
        token_method = "tiktoken/cl100k_base"
    except Exception:
        tokenizer = None

    for path in json_files:
        try:
            text = safe_read_text(path)
        except Exception:
            parse_failures += 1
            continue

        if tokenizer is not None and token_total is not None:
            token_total += len(tokenizer.encode(text))

        try:
            data = json.loads(text)
        except Exception:
            parse_failures += 1
            continue

        if isinstance(data, list):
            count = len(data)
        elif isinstance(data, dict):
            count = 1
        else:
            count = 0

        record_total += count
        record_counts_by_type[path.name] = record_counts_by_type.get(path.name, 0) + count

    return record_total, record_counts_by_type, token_total, token_method, parse_failures


def compute_statistics(repo_root: Path) -> Dict[str, Any]:
    all_files = [p for p in iter_paths(repo_root) if p.is_file()]
    all_dirs = [p for p in iter_paths(repo_root) if p.is_dir()]
    top_level_dirs = [p for p in repo_root.iterdir() if p.is_dir() and p.name != ".git"]
    json_files = [p for p in all_files if p.suffix.lower() == ".json"]

    total_size_bytes = sum(p.stat().st_size for p in all_files)
    avg_json_size = int(sum(p.stat().st_size for p in json_files) / len(json_files)) if json_files else 0

    emotional_root = repo_root / "sandhi-emotional-intelligence-dataset"
    spiritual_root = repo_root / "sandhi-spritual-intelligence-dataset"

    exclude_emotional = {"taxonomy", "sandhi_dataset_pipeline"}
    emotional_categories = [
        p for p in emotional_root.iterdir() if p.is_dir() and p.name not in exclude_emotional
    ]

    subcategory_dirs = []
    category_json_counts: Dict[str, int] = {}
    for category in emotional_categories:
        subcategory_dirs.extend([p for p in category.iterdir() if p.is_dir()])
        category_json_counts[category.name] = sum(
            1 for p in category.rglob("*.json") if p.is_file()
        )

    largest_category = min(
        category_json_counts.items(), key=lambda item: (-item[1], item[0].lower())
    )
    smallest_category = min(
        category_json_counts.items(), key=lambda item: (item[1], item[0].lower())
    )

    spiritual_collections = [p for p in spiritual_root.iterdir() if p.is_dir()]
    spiritual_collection_counts = {
        p.name: sum(1 for f in p.rglob("*.json") if f.is_file()) for p in spiritual_collections
    }

    section_paths = {
        "sandhi-emotional-intelligence-dataset": emotional_root,
        "sandhi-spritual-intelligence-dataset": spiritual_root,
    }
    section_stats = {}
    for name, path in section_paths.items():
        files = [p for p in path.rglob("*") if p.is_file()]
        section_stats[name] = {
            "file_count": len(files),
            "json_file_count": sum(1 for p in files if p.suffix.lower() == ".json"),
            "size_bytes": sum(p.stat().st_size for p in files),
        }
        section_stats[name]["size_human"] = human_bytes(section_stats[name]["size_bytes"])

    record_total, record_counts, token_total, token_method, parse_failures = (
        compute_records_and_tokens(json_files)
    )

    stats = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "paths": {
            "repository_root": str(repo_root.resolve()),
            "emotional_dataset": str(emotional_root.resolve()),
            "spiritual_dataset": str(spiritual_root.resolve()),
        },
        "counts": {
            "total_folders": len(all_dirs),
            "total_subfolders": len(all_dirs) - len(top_level_dirs),
            "total_files": len(all_files),
            "total_json_files": len(json_files),
            "total_dataset_size_bytes": total_size_bytes,
            "total_dataset_size_human": human_bytes(total_size_bytes),
            "average_json_file_size_bytes": avg_json_size,
            "average_json_file_size_human": human_bytes(avg_json_size),
            "category_count": len(emotional_categories),
            "subcategory_count": len(subcategory_dirs),
            "spiritual_collection_count": len(spiritual_collections),
            "total_records": record_total,
            "token_count": token_total,
            "token_count_method": token_method,
            "json_parse_failures": parse_failures,
        },
        "sections": section_stats,
        "categories": {
            "largest_by_json_files": {
                "name": largest_category[0],
                "json_file_count": largest_category[1],
                "section": "sandhi-emotional-intelligence-dataset",
            },
            "smallest_by_json_files": {
                "name": smallest_category[0],
                "json_file_count": smallest_category[1],
                "section": "sandhi-emotional-intelligence-dataset",
            },
        },
        "spiritual_collections": spiritual_collection_counts,
        "record_counts_by_json_type": record_counts,
    }

    return stats


def write_markdown(stats: Dict[str, Any], output_path: Path) -> None:
    counts = stats["counts"]
    sections = stats["sections"]

    token_note = (
        f"{counts['token_count']:,}" if counts["token_count"] is not None else "Not computed"
    )

    md_lines = [
        "# Dataset Statistics",
        "",
        f"Generated at: `{stats['generated_at']}`",
        "",
        "## Core Counts",
        "",
        f"- Total folders: {counts['total_folders']}",
        f"- Total subfolders: {counts['total_subfolders']}",
        f"- Total files: {counts['total_files']}",
        f"- Total JSON files: {counts['total_json_files']}",
        f"- Total dataset size: {counts['total_dataset_size_human']} ({counts['total_dataset_size_bytes']:,} bytes)",
        f"- Average JSON file size: {counts['average_json_file_size_human']} ({counts['average_json_file_size_bytes']:,} bytes)",
        f"- Emotional categories: {counts['category_count']}",
        f"- Emotional subcategories: {counts['subcategory_count']}",
        f"- Spiritual collections: {counts['spiritual_collection_count']}",
        f"- Total records (top-level JSON items): {counts['total_records']:,}",
        f"- Token count ({counts['token_count_method']}): {token_note}",
        "",
        "## Dataset Sections",
        "",
    ]

    for name, section in sections.items():
        md_lines.extend(
            [
                f"- **{name}**",
                f"  - Files: {section['file_count']}",
                f"  - JSON files: {section['json_file_count']}",
                f"  - Size: {section['size_human']} ({section['size_bytes']:,} bytes)",
            ]
        )

    md_lines.extend(
        [
            "",
            "## Category Extremes (Emotional Dataset)",
            "",
            f"- Largest category by JSON file count: **{stats['categories']['largest_by_json_files']['name']}** ({stats['categories']['largest_by_json_files']['json_file_count']} files)",
            f"- Smallest category by JSON file count: **{stats['categories']['smallest_by_json_files']['name']}** ({stats['categories']['smallest_by_json_files']['json_file_count']} files)",
            "",
            "## Spiritual Collections",
            "",
        ]
    )

    for name, count in sorted(stats["spiritual_collections"].items()):
        md_lines.append(f"- {name}: {count} JSON files")

    if counts["json_parse_failures"]:
        md_lines.extend(
            [
                "",
                "## Warnings",
                "",
                f"- JSON parse failures: {counts['json_parse_failures']}",
            ]
        )

    output_path.write_text("\n".join(md_lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute Sandhi dataset statistics.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to repository root.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Directory to write statistics.json and statistics.md",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    output_dir = args.output_dir.resolve()

    stats = compute_statistics(repo_root)

    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "statistics.json"
    md_path = output_dir / "statistics.md"

    json_path.write_text(json.dumps(stats, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(stats, md_path)

    print(f"Wrote {json_path} and {md_path}")


if __name__ == "__main__":
    main()
