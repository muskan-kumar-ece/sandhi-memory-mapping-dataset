# Schema Documentation

## Overview
This document describes the folder hierarchy, category/subcategory taxonomy, and JSON schemas used in the Sandhi Memory Mapping Dataset. Field descriptions and example schemas are derived from the repository JSON files.

## Dataset Sections
- `sandhi-emotional-intelligence-dataset/`: Emotional categories and subcategories with structured inputs, responses, evaluations, and memory patterns.
- `sandhi-spritual-intelligence-dataset/`: Spiritual wisdom entries organized by collection.
- `sandhi-emotional-intelligence-dataset/sandhi_dataset_pipeline/`: Pipeline inputs/outputs for generating structured emotional data.

## Full Folder Hierarchy (Directories)
```text
sandhi-memory-mapping-dataset/
  sandhi-emotional-intelligence-dataset/
    Abandonment Issues/
      clinginess/
      fear_of_rejection/
      hypervigilance/
      jealousy/
      pushing_people_away/
    Academic Apathy/
      boredom/
      burnout/
      disillusionment/
      lack_of_purpose/
      procrastination/
    Academic Pressure/
      competition/
      family_academic_expectations/
      fear_of_failing/
      grade_anxiety/
      grade_obsession/
      parental_expectations/
      scholarship_stress/
    Academic Validation Seeking/
      burnout/
      competition/
      fear_of_failure/
      perfectionism/
      self_worth_tied_to_grades/
    Anger Management/
      explosive_outbursts/
      irritability/
      passive_aggression/
      regret/
      resentment/
    Anticipatory Anxiety/
      dread/
      overplanning/
      physical_tension/
      restlessness/
      worst_case_scenarios/
    Anxiety about Public Speaking/
      avoidance/
      fear_of_judgment/
      perfectionism/
      physical_symptoms/
      stage_fright/
    Apathy Towards Future/
      burnout/
      cynicism/
      depression/
      hopelessness/
      lack_of_motivation/
    Attachment Issues/
      anxious_attachment/
      avoidant_attachment/
      clinginess/
      fear_of_intimacy/
      trust_issues/
    Body Dysmorphia/
      avoidance/
      comparison/
      obsessive_checking/
      perfectionism/
      shame/
    Body Image Issues/
      avoidance_of_socials/
      body_checking_habit/
      comparison/
      dysmorphia/
      eating_disorders/
      low_self_esteem/
      obsessive_checking/
    Burnout/
      cynicism/
      depersonalization/
      detachment/
      emotional_drain/
      exhaustion/
      physical_exhaustion/
      reduced_efficacy/
    Career Indecision/
      analysis_paralysis/
      fear_of_wrong_choice/
      overwhelm/
      parental_pressure/
      passion_vs_money/
    Chronic Boredom/
      apathy/
      dissatisfaction/
      dopamine_seeking/
      lack_of_purpose/
      restlessness/
    Chronic Fatigue/
      apathy/
      brain_fog/
      exhaustion/
      low_motivation/
      physical_weakness/
    Chronic Indecision/
      analysis_paralysis/
      anxiety/
      dependence_on_others/
      fear_of_regret/
      overthinking/
    Climate Anxiety/
      anger/
      existential_dread/
      grief/
      helplessness/
      hopelessness/
    Codependency/
      enmeshment/
      fear_of_abandonment/
      loss_of_identity/
      people_pleasing/
      resentment/
    Comparison/
      academic_comparison/
      body_image_issues/
      inferiority_complex/
      jealousy/
      peer_envy/
      relative_deprivation/
      social_media_envy/
    Conflict Avoidance/
      fear_of_anger/
      passive_aggression/
      people_pleasing/
      resentment/
      suppression/
    Creative Block/
      burnout/
      fear_of_judgment/
      imposter_syndrome/
      lack_of_inspiration/
      perfectionism/
    Creative Burnout/
      apathy/
      exhaustion/
      frustration/
      imposter_syndrome/
      lack_of_ideas/
    Cultural Disconnect/
      alienation/
      code_switching_fatigue/
      identity_crisis/
      loneliness/
      misunderstanding/
    Cyberbullying Trauma/
      anxiety/
      low_self_esteem/
      paranoia/
      social_withdrawal/
      trust_issues/
    Decision Fatigue/
      avoidance/
      brain_fog/
      impulsivity/
      overwhelm/
      procrastination/
    Diet Culture Anxiety/
      body_checking/
      comparison/
      fear_of_weight_gain/
      food_guilt/
      obsessive_tracking/
    Difficulty Communicating/
      anxiety/
      fear_of_conflict/
      misunderstanding/
      stuttering/
      suppression/
    Difficulty Making Friends/
      awkwardness/
      fear_of_rejection/
      isolation/
      loneliness/
      social_anxiety/
    Difficulty Setting Boundaries/
      burnout/
      fear_of_conflict/
      guilt/
      people_pleasing/
      resentment/
    Discipline Problems/
      attention_drift/
      distraction/
      instant_gratification/
      instant_gratification_habit/
      lack_of_routine/
      poor_time_management/
      procrastination/
    Disconnection from Reality/
      brain_fog/
      depersonalization/
      derealization/
      dissociation/
      numbness/
    Disillusionment/
      apathy/
      cynicism/
      loss_of_trust/
      resentment/
      sadness/
    Emotional Exhaustion/
      burnout/
      compassion_fatigue/
      irritability/
      numbness/
      withdrawal/
    Emotional Numbness/
      anhedonia/
      anhedonia_symptoms/
      apathy/
      burnout/
      dissociation/
      dissociative_states/
      trauma_response/
    Emotional Vulnerability/
      defensiveness/
      fear_of_rejection/
      intimacy_issues/
      oversharing/
      shame/
    Empathy Overload/
      absorbing_emotions/
      boundaries_issues/
      burnout/
      compassion_fatigue/
      exhaustion/
    Exam Anxiety/
      burnout/
      concentration_problem/
      fear_of_failing/
      low_confidence/
      panic_before_exam/
      parental_pressure/
      physical_panic_symptoms/
      time_pressure/
    Existential Dread/
      fear_of_death/
      insignificance/
      isolation/
      meaninglessness/
      overthinking/
    Existential Loneliness/
      alienation/
      despair/
      disconnect/
      isolation/
      meaninglessness/
    Fear of Abandonment/
      clinginess/
      hypervigilance/
      jealousy/
      panic/
      people_pleasing/
    Fear of Commitment/
      anxiety/
      avoidance/
      feeling_trapped/
      self_sabotage/
      trust_issues/
    Fear of Disappointing Others/
      anxiety/
      burnout/
      guilt/
      people_pleasing/
      perfectionism/
    Fear of Failure/
      avoidance/
      fear_of_judgment/
      imposter_syndrome/
      low_self_worth/
      perceived_incompetence/
      perfectionism/
      shame_avoidance/
    Fear of Intimacy/
      avoidance/
      emotional_walls/
      fear_of_vulnerability/
      sabotaging_relationships/
      trust_issues/
    Fear of Judgment/
      hiding_true_self/
      overthinking/
      people_pleasing/
      perfectionism/
      social_anxiety/
    Fear of the Unknown/
      anxiety/
      control_issues/
      overthinking/
      paralysis/
      resistance_to_change/
    Feeling Empty/
      anhedonia/
      depression/
      loneliness/
      loss_of_identity/
      numbness/
    Feeling Inadequate/
      comparison/
      fear_of_failure/
      imposter_syndrome/
      low_self_esteem/
      perfectionism/
    Feeling Left Behind/
      comparison/
      fomo/
      inferiority/
      loneliness/
      timeline_anxiety/
    Feeling Misunderstood/
      alienation/
      communication_gap/
      expressive_block/
      frustration/
      isolation/
      lack_of_empathetic_support/
      loneliness/
    Feeling Out of Place/
      alienation/
      awkwardness/
      cultural_disconnect/
      imposter_syndrome/
      loneliness/
    Feeling Overwhelmed/
      anxiety/
      brain_fog/
      burnout/
      paralysis/
      procrastination/
    Feeling Unappreciated/
      burnout/
      low_self_worth/
      passive_aggression/
      resentment/
      withdrawal/
    Feeling Unattractive/
      body_dysmorphia/
      comparison/
      low_self_esteem/
      rejection_sensitivity/
      social_withdrawal/
    Feeling Unlovable/
      depression/
      low_self_worth/
      rejection_sensitivity/
      self_isolation/
      settling/
    Feeling Unseen/
      alienation/
      frustration/
      invalidation/
      loneliness/
      low_self_worth/
    Financial Insecurity/
      comparison/
      panic/
      shame/
      sleep_deprivation/
      survival_mode/
    Financial Stress/
      budgeting_fear/
      comparison/
      debt_anxiety/
      job_insecurity/
      loan_repayment_anxiety/
      scarcity_mindset/
      survival_mode/
    First-Generation Student Pressure/
      family_expectations/
      fear_of_failure/
      financial_guilt/
      imposter_syndrome/
      isolation/
    FOMO (Fear of Missing Out)/
      compulsive_checking/
      dissatisfaction/
      exclusion_sadness/
      jealousy/
      overcommitment/
      restlessness/
      social_media_anxiety/
    Frustration with Lack of Progress/
      burnout/
      comparison/
      hopelessness/
      impatience/
      self_doubt/
    Future Uncertainty/
      career_anxiety/
      decision_paralysis/
      existential_dread/
      existential_paralysis/
      fear_of_unknown/
      financial_fears/
      financial_survival_anxiety/
    Grief and Loss/
      acute_grief/
      anger/
      complicated_bereavement/
      denial/
      empty_feeling/
      nostalgia/
      sadness/
    Guilt over Past Mistakes/
      apology_overload/
      inability_to_move_on/
      rumination/
      self_sabotage/
      shame/
    Heartbreak/
      betrayal/
      denial_and_bargaining/
      emotional_triggering/
      grief/
      loss_of_identity/
      trust_issues/
      unrequited_love/
    Homesickness/
      adjustment_fatigue/
      cultural_disconnect/
      family_attachment/
      grief_for_familiarity/
      isolation/
      loneliness/
      nostalgia/
    Hopelessness/
      apathy/
      depression/
      despair/
      giving_up/
      numbness/
    Hyper-independence/
      burnout/
      difficulty_asking_for_help/
      fear_of_vulnerability/
      isolation/
      trust_issues/
    Identity Crisis/
      chameleon_behavior/
      existential_dread/
      existential_vacuum/
      lost_sense_of_self/
      role_confusion/
      value_conflict/
      value_disorientation/
    Impatience/
      anxiety/
      frustration/
      irritability/
      restlessness/
      rushing/
    Imposter Syndrome/
      discounting_success/
      externalizing_success/
      fear_of_exposure/
      fraud_feeling/
      overworking/
      perfectionism/
      perfectionism_trap/
    Inability to Focus/
      adhd_symptoms/
      brain_fog/
      burnout/
      distraction/
      procrastination/
    Inferiority Complex/
      comparison/
      jealousy/
      low_self_esteem/
      overcompensating/
      social_withdrawal/
    Intrusive Thoughts/
      anxiety/
      compulsions/
      fear_of_losing_control/
      guilt/
      obsessions/
    Jealousy/
      comparison/
      fear_of_loss/
      insecurity/
      possessiveness/
      resentment/
    Job Search Depression/
      financial_stress/
      hopelessness/
      imposter_syndrome/
      loss_of_identity/
      rejection_fatigue/
    Lack of Motivation/
      apathy/
      burnout/
      executive_dysfunction/
      mental_fatigue/
      no_clear_goals/
      overwhelmed/
      procrastination/
    Lack of Self-Esteem/
      comparison/
      fear_of_rejection/
      insecurity/
      negative_self_talk/
      people_pleasing/
    Loneliness/
      breakup_loneliness/
      emotional_disconnection/
      isolation/
      lack_of_belonging/
      no_friends/
      social_anxiety/
      social_media_isolation/
    Long-distance Relationship Strain/
      communication_fatigue/
      frustration/
      insecurity/
      jealousy/
      loneliness/
    Loss of a Pet/
      empty_house_syndrome/
      grief/
      guilt/
      heartbreak/
      loneliness/
    Loss of Control/
      anger/
      anxiety/
      helplessness/
      micromanaging/
      panic/
    Loss of Identity in a Relationship/
      codependency/
      enmeshment/
      loss_of_hobbies/
      people_pleasing/
      resentment/
    Loss of Passion/
      apathy/
      burnout/
      disillusionment/
      grief/
      identity_crisis/
    Mood Swings/
      confusion/
      emotional_instability/
      exhaustion/
      irritability/
      unpredictability/
    Nostalgia - Stuck in the Past/
      idealization/
      regret/
      resistance_to_change/
      rumination/
      sadness/
    Nostalgic Sadness/
      dissatisfaction_with_present/
      grief/
      loneliness/
      longing/
      stuck_in_past/
    Overcommitment Stress/
      burnout/
      drop_in_quality/
      exhaustion/
      inability_to_say_no/
      resentment/
    Overthinking/
      catastrophizing/
      decision_paralysis/
      future_worry/
      insomnia/
      past_regrets/
      rumination/
      worst_case_scenarios/
    Pandemic-related Social Regression/
      awkwardness/
      fear_of_crowds/
      isolation/
      loss_of_skills/
      social_anxiety/
    Paranoia (Social - Relational)/
      fear_of_betrayal/
      hypervigilance/
      isolation/
      suspicion/
      trust_issues/
    Parental Pressure/
      anxiety/
      fear_of_disappointing/
      perfectionism/
      rebellion/
      resentment/
    Peer Pressure/
      anxiety/
      compromising_values/
      conformity/
      fear_of_missing_out/
      resentment/
    People-Pleasing/
      boundary_issues/
      burnout/
      fear_of_conflict/
      loss_of_identity/
      resentment/
    Perfectionism/
      all_or_nothing_thinking/
      burnout/
      fear_of_making_mistakes/
      fear_of_mistakes/
      procrastination/
      unforgiving_standards/
      unrealistic_standards/
    Performance Anxiety/
      blanking_out/
      fear_of_judgment/
      negative_self_talk/
      perfectionism/
      shaking/
      somatic_hyperarousal/
      stage_fright/
    Post-project Empty Feeling/
      anhedonia/
      anticlimax/
      boredom/
      burnout/
      loss_of_purpose/
    Post-vacation Blues/
      dread/
      exhaustion/
      lack_of_motivation/
      nostalgia/
      sadness/
    Procrastination Guilt/
      avoidance_cycle/
      guilt_cycle/
      last_minute_panic/
      overwhelm/
      self_criticism/
      shame/
      task_aversion/
    Purpose Confusion/
      career_indecision/
      existential_dread/
      expectation_mismatch/
      feeling_lost/
      identity_drift/
      meaninglessness/
      quarter_life_crisis/
    Quarter-Life Crisis/
      career_doubt/
      comparison/
      financial_fear/
      identity_confusion/
      relationship_pressure/
    Quarter-system Burnout (Academic)/
      academic_pressure/
      constant_stress/
      cramming/
      exhaustion/
      no_breaks/
    Regret/
      rumination/
      sadness/
      self_blame/
      stuck_in_past/
      what_ifs/
    Regret over Wasted Time/
      comparison/
      depression/
      panic_about_future/
      self_loathing/
      shame/
    Rejection Sensitivity/
      emotional_flashbacks/
      fear_of_abandonment/
      hypervigilance/
      hypervigilance_for_rejection/
      overreacting/
      people_pleasing/
      social_withdrawal/
    Relationship Conflicts/
      boundary_crossing/
      communication_issues/
      fear_of_abandonment/
      resentment/
      stonewalling/
      trust_erosion/
      trust_issues/
    Religious Trauma/
      anger/
      fear_of_punishment/
      guilt/
      identity_crisis/
      loss_of_community/
    Resentment/
      anger/
      bitterness/
      feeling_unfairly_treated/
      grudges/
      passive_aggression/
    Romantic Obsession/
      anxiety/
      fear_of_rejection/
      jealousy/
      limerence/
      loss_of_focus/
    sandhi_dataset_pipeline/
      outputs/
      processed_data/
      raw_data/
      scripts/
    Self-Doubt/
      fear_of_failing/
      fear_of_success/
      imposter_syndrome/
      imposter_triggers/
      insecurity/
      need_for_validation/
      repeated_failure/
      second_guessing/
      self_deprecating_talk/
    Self-Sabotage/
      destructive_habits/
      fear_of_success/
      imposter_syndrome/
      procrastination/
      unworthiness/
    Sensory Overload/
      brain_fog/
      exhaustion/
      irritability/
      panic/
      withdrawal/
    Separation Anxiety/
      clinginess/
      fear_of_loss/
      hypervigilance/
      panic/
      sleeplessness/
    Shame/
      fear_of_exposure/
      hiding/
      perfectionism/
      self_hatred/
      withdrawal/
    Sleep Deprivation Brain Fog/
      circadian_disruption/
      cognitive_slowing/
      fatigue/
      irritability/
      memory_issues/
      mood_swings/
      poor_focus/
    Social Anxiety/
      avoidance/
      awkwardness/
      fear_of_judgment/
      negative_evaluation_fear/
      overthinking_interactions/
      post_event_rumination/
      public_speaking_fear/
    Social Battery Depletion/
      brain_fog/
      exhaustion/
      introvert_burnout/
      irritability/
      withdrawal/
    Social Isolation/
      apathy/
      depression/
      fear_of_rejection/
      loneliness/
      withdrawal/
    Spiritual Crisis/
      alienation/
      confusion/
      existential_dread/
      guilt/
      loss_of_faith/
    Success Anxiety/
      burnout/
      fear_of_expectations/
      imposter_syndrome/
      pressure/
      self_sabotage/
    taxonomy/
    Technology Addiction/
      distraction/
      doomscrolling/
      fomo/
      screen_time_guilt/
      sleep_disruption/
    Toxic Friendship Dynamics/
      competition/
      drain/
      gossip/
      manipulation/
      walking_on_eggshells/
    Toxic Positivity Exhaustion/
      alienation/
      burnout/
      guilt/
      invalidation/
      suppression/
    Transitioning to Adulthood/
      fear_of_responsibility/
      imposter_syndrome/
      loneliness/
      nostalgia/
      overwhelm/
    Trust Betrayal Trauma/
      emotional_walls/
      fear_of_intimacy/
      hypervigilance/
      jealousy/
      paranoia/
    Trust Issues/
      avoidance/
      fear_of_betrayal/
      fear_of_dependence/
      hypervigilance/
      jealousy/
      suspicion_habit/
      testing_partners/
    Unrealistic Expectations/
      burnout/
      comparison/
      disappointment/
      perfectionism/
      pressure/
    Unrequited Love/
      grief/
      idealization/
      jealousy/
      low_self_worth/
      obsession/
    Work-Life Imbalance/
      burnout/
      exhaustion/
      guilt/
      loss_of_identity/
      relationship_strain/
    Workplace Bullying Stress/
      anxiety/
      burnout/
      dread/
      low_self_esteem/
      paranoia/
  sandhi-spritual-intelligence-dataset/
    hitopadesa/
      the_book_of_good_counsels/
    mahabharata/
      the_mahabharata/
    pursuit-of-god/
      the_pursuit_of_god/
    swami-sivananda/
      20_important_spiritual_instructions/
      bliss_divine/
      important_spiritual_instructions/
    yoga-sutras/
      the_yoga_sutras_of_patanjali/
```

## Category Hierarchy (Emotional Dataset)
- Abandonment Issues
- Academic Apathy
- Academic Pressure
- Academic Validation Seeking
- Anger Management
- Anticipatory Anxiety
- Anxiety about Public Speaking
- Apathy Towards Future
- Attachment Issues
- Body Dysmorphia
- Body Image Issues
- Burnout
- Career Indecision
- Chronic Boredom
- Chronic Fatigue
- Chronic Indecision
- Climate Anxiety
- Codependency
- Comparison
- Conflict Avoidance
- Creative Block
- Creative Burnout
- Cultural Disconnect
- Cyberbullying Trauma
- Decision Fatigue
- Diet Culture Anxiety
- Difficulty Communicating
- Difficulty Making Friends
- Difficulty Setting Boundaries
- Discipline Problems
- Disconnection from Reality
- Disillusionment
- Emotional Exhaustion
- Emotional Numbness
- Emotional Vulnerability
- Empathy Overload
- Exam Anxiety
- Existential Dread
- Existential Loneliness
- Fear of Abandonment
- Fear of Commitment
- Fear of Disappointing Others
- Fear of Failure
- Fear of Intimacy
- Fear of Judgment
- Fear of the Unknown
- Feeling Empty
- Feeling Inadequate
- Feeling Left Behind
- Feeling Misunderstood
- Feeling Out of Place
- Feeling Overwhelmed
- Feeling Unappreciated
- Feeling Unattractive
- Feeling Unlovable
- Feeling Unseen
- Financial Insecurity
- Financial Stress
- First-Generation Student Pressure
- FOMO (Fear of Missing Out)
- Frustration with Lack of Progress
- Future Uncertainty
- Grief and Loss
- Guilt over Past Mistakes
- Heartbreak
- Homesickness
- Hopelessness
- Hyper-independence
- Identity Crisis
- Impatience
- Imposter Syndrome
- Inability to Focus
- Inferiority Complex
- Intrusive Thoughts
- Jealousy
- Job Search Depression
- Lack of Motivation
- Lack of Self-Esteem
- Loneliness
- Long-distance Relationship Strain
- Loss of a Pet
- Loss of Control
- Loss of Identity in a Relationship
- Loss of Passion
- Mood Swings
- Nostalgia - Stuck in the Past
- Nostalgic Sadness
- Overcommitment Stress
- Overthinking
- Pandemic-related Social Regression
- Paranoia (Social - Relational)
- Parental Pressure
- Peer Pressure
- People-Pleasing
- Perfectionism
- Performance Anxiety
- Post-project Empty Feeling
- Post-vacation Blues
- Procrastination Guilt
- Purpose Confusion
- Quarter-Life Crisis
- Quarter-system Burnout (Academic)
- Regret
- Regret over Wasted Time
- Rejection Sensitivity
- Relationship Conflicts
- Religious Trauma
- Resentment
- Romantic Obsession
- Self-Doubt
- Self-Sabotage
- Sensory Overload
- Separation Anxiety
- Shame
- Sleep Deprivation Brain Fog
- Social Anxiety
- Social Battery Depletion
- Social Isolation
- Spiritual Crisis
- Success Anxiety
- Technology Addiction
- Toxic Friendship Dynamics
- Toxic Positivity Exhaustion
- Transitioning to Adulthood
- Trust Betrayal Trauma
- Trust Issues
- Unrealistic Expectations
- Unrequited Love
- Work-Life Imbalance
- Workplace Bullying Stress

## Subcategory Hierarchy (Emotional Dataset)
- Abandonment Issues
  - clinginess
  - pushing_people_away
  - fear_of_rejection
  - jealousy
  - hypervigilance
- Academic Apathy
  - burnout
  - lack_of_purpose
  - procrastination
  - boredom
  - disillusionment
- Academic Pressure
  - grade_anxiety
  - parental_expectations
  - competition
  - scholarship_stress
  - fear_of_failing
  - grade_obsession
  - family_academic_expectations
- Academic Validation Seeking
  - burnout
  - self_worth_tied_to_grades
  - competition
  - fear_of_failure
  - perfectionism
- Anger Management
  - explosive_outbursts
  - resentment
  - irritability
  - passive_aggression
  - regret
- Anticipatory Anxiety
  - worst_case_scenarios
  - restlessness
  - overplanning
  - physical_tension
  - dread
- Anxiety about Public Speaking
  - stage_fright
  - physical_symptoms
  - avoidance
  - perfectionism
  - fear_of_judgment
- Apathy Towards Future
  - hopelessness
  - burnout
  - depression
  - lack_of_motivation
  - cynicism
- Attachment Issues
  - anxious_attachment
  - avoidant_attachment
  - fear_of_intimacy
  - clinginess
  - trust_issues
- Body Dysmorphia
  - obsessive_checking
  - avoidance
  - shame
  - comparison
  - perfectionism
- Body Image Issues
  - dysmorphia
  - eating_disorders
  - comparison
  - low_self_esteem
  - obsessive_checking
  - body_checking_habit
  - avoidance_of_socials
- Burnout
  - exhaustion
  - cynicism
  - reduced_efficacy
  - emotional_drain
  - detachment
  - physical_exhaustion
  - depersonalization
- Career Indecision
  - fear_of_wrong_choice
  - overwhelm
  - passion_vs_money
  - parental_pressure
  - analysis_paralysis
- Chronic Boredom
  - apathy
  - restlessness
  - dissatisfaction
  - lack_of_purpose
  - dopamine_seeking
- Chronic Fatigue
  - exhaustion
  - low_motivation
  - brain_fog
  - physical_weakness
  - apathy
- Chronic Indecision
  - fear_of_regret
  - overthinking
  - analysis_paralysis
  - dependence_on_others
  - anxiety
- Climate Anxiety
  - existential_dread
  - helplessness
  - anger
  - grief
  - hopelessness
- Codependency
  - loss_of_identity
  - fear_of_abandonment
  - enmeshment
  - people_pleasing
  - resentment
- Comparison
  - social_media_envy
  - inferiority_complex
  - body_image_issues
  - academic_comparison
  - jealousy
  - peer_envy
  - relative_deprivation
- Conflict Avoidance
  - suppression
  - passive_aggression
  - fear_of_anger
  - people_pleasing
  - resentment
- Creative Block
  - perfectionism
  - burnout
  - fear_of_judgment
  - imposter_syndrome
  - lack_of_inspiration
- Creative Burnout
  - exhaustion
  - lack_of_ideas
  - frustration
  - apathy
  - imposter_syndrome
- Cultural Disconnect
  - alienation
  - identity_crisis
  - loneliness
  - code_switching_fatigue
  - misunderstanding
- Cyberbullying Trauma
  - trust_issues
  - social_withdrawal
  - paranoia
  - low_self_esteem
  - anxiety
- Decision Fatigue
  - overwhelm
  - avoidance
  - impulsivity
  - brain_fog
  - procrastination
- Diet Culture Anxiety
  - food_guilt
  - body_checking
  - obsessive_tracking
  - fear_of_weight_gain
  - comparison
- Difficulty Communicating
  - fear_of_conflict
  - stuttering
  - misunderstanding
  - suppression
  - anxiety
- Difficulty Making Friends
  - social_anxiety
  - awkwardness
  - loneliness
  - fear_of_rejection
  - isolation
- Difficulty Setting Boundaries
  - people_pleasing
  - resentment
  - burnout
  - fear_of_conflict
  - guilt
- Discipline Problems
  - procrastination
  - distraction
  - lack_of_routine
  - instant_gratification
  - poor_time_management
  - attention_drift
  - instant_gratification_habit
- Disconnection from Reality
  - dissociation
  - depersonalization
  - derealization
  - numbness
  - brain_fog
- Disillusionment
  - cynicism
  - loss_of_trust
  - apathy
  - sadness
  - resentment
- Emotional Exhaustion
  - compassion_fatigue
  - burnout
  - numbness
  - irritability
  - withdrawal
- Emotional Numbness
  - apathy
  - dissociation
  - burnout
  - trauma_response
  - anhedonia
  - dissociative_states
  - anhedonia_symptoms
- Emotional Vulnerability
  - fear_of_rejection
  - oversharing
  - shame
  - defensiveness
  - intimacy_issues
- Empathy Overload
  - compassion_fatigue
  - burnout
  - absorbing_emotions
  - boundaries_issues
  - exhaustion
- Exam Anxiety
  - fear_of_failing
  - parental_pressure
  - low_confidence
  - panic_before_exam
  - burnout
  - concentration_problem
  - physical_panic_symptoms
  - time_pressure
- Existential Dread
  - meaninglessness
  - fear_of_death
  - insignificance
  - isolation
  - overthinking
- Existential Loneliness
  - alienation
  - meaninglessness
  - isolation
  - disconnect
  - despair
- Fear of Abandonment
  - clinginess
  - jealousy
  - people_pleasing
  - hypervigilance
  - panic
- Fear of Commitment
  - avoidance
  - feeling_trapped
  - trust_issues
  - self_sabotage
  - anxiety
- Fear of Disappointing Others
  - people_pleasing
  - guilt
  - perfectionism
  - burnout
  - anxiety
- Fear of Failure
  - perfectionism
  - avoidance
  - imposter_syndrome
  - fear_of_judgment
  - low_self_worth
  - shame_avoidance
  - perceived_incompetence
- Fear of Intimacy
  - avoidance
  - emotional_walls
  - fear_of_vulnerability
  - sabotaging_relationships
  - trust_issues
- Fear of Judgment
  - social_anxiety
  - people_pleasing
  - perfectionism
  - hiding_true_self
  - overthinking
- Fear of the Unknown
  - control_issues
  - anxiety
  - resistance_to_change
  - overthinking
  - paralysis
- Feeling Empty
  - anhedonia
  - numbness
  - loneliness
  - depression
  - loss_of_identity
- Feeling Inadequate
  - imposter_syndrome
  - comparison
  - low_self_esteem
  - perfectionism
  - fear_of_failure
- Feeling Left Behind
  - comparison
  - fomo
  - timeline_anxiety
  - inferiority
  - loneliness
- Feeling Misunderstood
  - alienation
  - frustration
  - loneliness
  - communication_gap
  - isolation
  - lack_of_empathetic_support
  - expressive_block
- Feeling Out of Place
  - alienation
  - imposter_syndrome
  - awkwardness
  - loneliness
  - cultural_disconnect
- Feeling Overwhelmed
  - paralysis
  - burnout
  - anxiety
  - brain_fog
  - procrastination
- Feeling Unappreciated
  - resentment
  - burnout
  - low_self_worth
  - withdrawal
  - passive_aggression
- Feeling Unattractive
  - body_dysmorphia
  - comparison
  - low_self_esteem
  - rejection_sensitivity
  - social_withdrawal
- Feeling Unlovable
  - low_self_worth
  - rejection_sensitivity
  - self_isolation
  - settling
  - depression
- Feeling Unseen
  - loneliness
  - invalidation
  - frustration
  - alienation
  - low_self_worth
- Financial Insecurity
  - survival_mode
  - panic
  - shame
  - comparison
  - sleep_deprivation
- Financial Stress
  - debt_anxiety
  - job_insecurity
  - budgeting_fear
  - comparison
  - survival_mode
  - scarcity_mindset
  - loan_repayment_anxiety
- First-Generation Student Pressure
  - imposter_syndrome
  - family_expectations
  - financial_guilt
  - isolation
  - fear_of_failure
- FOMO
  - social_media_anxiety
  - overcommitment
  - jealousy
  - restlessness
  - dissatisfaction
  - compulsive_checking
  - exclusion_sadness
- Frustration with Lack of Progress
  - impatience
  - comparison
  - burnout
  - self_doubt
  - hopelessness
- Future Uncertainty
  - career_anxiety
  - financial_fears
  - decision_paralysis
  - fear_of_unknown
  - existential_dread
  - existential_paralysis
  - financial_survival_anxiety
- Grief and Loss
  - denial
  - anger
  - sadness
  - empty_feeling
  - nostalgia
  - acute_grief
  - complicated_bereavement
- Guilt over Past Mistakes
  - rumination
  - shame
  - self_sabotage
  - apology_overload
  - inability_to_move_on
- Heartbreak
  - unrequited_love
  - betrayal
  - loss_of_identity
  - grief
  - trust_issues
  - denial_and_bargaining
  - emotional_triggering
- Homesickness
  - nostalgia
  - isolation
  - cultural_disconnect
  - family_attachment
  - loneliness
  - grief_for_familiarity
  - adjustment_fatigue
- Hopelessness
  - despair
  - depression
  - apathy
  - giving_up
  - numbness
- Hyper-independence
  - fear_of_vulnerability
  - trust_issues
  - burnout
  - isolation
  - difficulty_asking_for_help
- Identity Crisis
  - role_confusion
  - value_conflict
  - existential_dread
  - chameleon_behavior
  - lost_sense_of_self
  - value_disorientation
  - existential_vacuum
- Impatience
  - frustration
  - irritability
  - restlessness
  - rushing
  - anxiety
- Imposter Syndrome
  - fraud_feeling
  - discounting_success
  - overworking
  - fear_of_exposure
  - perfectionism
  - externalizing_success
  - perfectionism_trap
- Inability to Focus
  - brain_fog
  - distraction
  - adhd_symptoms
  - burnout
  - procrastination
- Inferiority Complex
  - comparison
  - low_self_esteem
  - overcompensating
  - social_withdrawal
  - jealousy
- Intrusive Thoughts
  - obsessions
  - anxiety
  - fear_of_losing_control
  - guilt
  - compulsions
- Jealousy
  - insecurity
  - comparison
  - possessiveness
  - fear_of_loss
  - resentment
- Job Search Depression
  - rejection_fatigue
  - imposter_syndrome
  - hopelessness
  - loss_of_identity
  - financial_stress
- Lack of Motivation
  - procrastination
  - apathy
  - burnout
  - overwhelmed
  - no_clear_goals
  - executive_dysfunction
  - mental_fatigue
- Lack of Self-Esteem
  - negative_self_talk
  - comparison
  - people_pleasing
  - insecurity
  - fear_of_rejection
- Loneliness
  - no_friends
  - emotional_disconnection
  - breakup_loneliness
  - social_anxiety
  - isolation
  - social_media_isolation
  - lack_of_belonging
- Long-distance Relationship Strain
  - loneliness
  - jealousy
  - communication_fatigue
  - insecurity
  - frustration
- Loss of a Pet
  - grief
  - loneliness
  - guilt
  - empty_house_syndrome
  - heartbreak
- Loss of Control
  - panic
  - micromanaging
  - anxiety
  - helplessness
  - anger
- Loss of Identity in a Relationship
  - enmeshment
  - codependency
  - people_pleasing
  - loss_of_hobbies
  - resentment
- Loss of Passion
  - burnout
  - apathy
  - grief
  - disillusionment
  - identity_crisis
- Mood Swings
  - emotional_instability
  - irritability
  - unpredictability
  - exhaustion
  - confusion
- Nostalgia / Stuck in the Past
  - rumination
  - idealization
  - sadness
  - resistance_to_change
  - regret
- Nostalgic Sadness
  - longing
  - grief
  - stuck_in_past
  - dissatisfaction_with_present
  - loneliness
- Overcommitment Stress
  - burnout
  - inability_to_say_no
  - exhaustion
  - resentment
  - drop_in_quality
- Overthinking
  - rumination
  - worst_case_scenarios
  - decision_paralysis
  - insomnia
  - past_regrets
  - catastrophizing
  - future_worry
- Pandemic-related Social Regression
  - social_anxiety
  - awkwardness
  - isolation
  - loss_of_skills
  - fear_of_crowds
- Paranoia (Social/Relational)
  - suspicion
  - hypervigilance
  - trust_issues
  - fear_of_betrayal
  - isolation
- Parental Pressure
  - fear_of_disappointing
  - perfectionism
  - rebellion
  - resentment
  - anxiety
- Peer Pressure
  - conformity
  - fear_of_missing_out
  - compromising_values
  - anxiety
  - resentment
- People-Pleasing
  - boundary_issues
  - fear_of_conflict
  - loss_of_identity
  - burnout
  - resentment
- Perfectionism
  - unrealistic_standards
  - fear_of_mistakes
  - all_or_nothing_thinking
  - procrastination
  - burnout
  - unforgiving_standards
  - fear_of_making_mistakes
- Performance Anxiety
  - stage_fright
  - fear_of_judgment
  - shaking
  - blanking_out
  - perfectionism
  - somatic_hyperarousal
  - negative_self_talk
- Post-project Empty Feeling
  - loss_of_purpose
  - anhedonia
  - burnout
  - anticlimax
  - boredom
- Post-vacation Blues
  - sadness
  - lack_of_motivation
  - dread
  - nostalgia
  - exhaustion
- Procrastination Guilt
  - shame
  - avoidance_cycle
  - last_minute_panic
  - self_criticism
  - overwhelm
  - task_aversion
  - guilt_cycle
- Purpose Confusion
  - existential_dread
  - career_indecision
  - feeling_lost
  - meaninglessness
  - quarter_life_crisis
  - identity_drift
  - expectation_mismatch
- Quarter-Life Crisis
  - career_doubt
  - relationship_pressure
  - financial_fear
  - identity_confusion
  - comparison
- Quarter-system Burnout
  - academic_pressure
  - exhaustion
  - no_breaks
  - constant_stress
  - cramming
- Regret
  - rumination
  - what_ifs
  - self_blame
  - sadness
  - stuck_in_past
- Regret over Wasted Time
  - shame
  - panic_about_future
  - comparison
  - self_loathing
  - depression
- Rejection Sensitivity
  - fear_of_abandonment
  - overreacting
  - people_pleasing
  - hypervigilance
  - social_withdrawal
  - hypervigilance_for_rejection
  - emotional_flashbacks
- Relationship Conflicts
  - communication_issues
  - trust_issues
  - boundary_crossing
  - resentment
  - fear_of_abandonment
  - stonewalling
  - trust_erosion
- Religious Trauma
  - guilt
  - fear_of_punishment
  - loss_of_community
  - anger
  - identity_crisis
- Resentment
  - grudges
  - passive_aggression
  - bitterness
  - feeling_unfairly_treated
  - anger
- Romantic Obsession
  - limerence
  - jealousy
  - loss_of_focus
  - anxiety
  - fear_of_rejection
- Self-Doubt
  - imposter_syndrome
  - second_guessing
  - need_for_validation
  - insecurity
  - fear_of_success
  - imposter_triggers
  - self_deprecating_talk
  - repeated_failure
  - fear_of_failing
- Self-Sabotage
  - fear_of_success
  - procrastination
  - imposter_syndrome
  - destructive_habits
  - unworthiness
- Sensory Overload
  - irritability
  - panic
  - exhaustion
  - withdrawal
  - brain_fog
- Separation Anxiety
  - clinginess
  - panic
  - fear_of_loss
  - hypervigilance
  - sleeplessness
- Shame
  - hiding
  - self_hatred
  - fear_of_exposure
  - withdrawal
  - perfectionism
- Sleep Deprivation Brain Fog
  - poor_focus
  - irritability
  - memory_issues
  - fatigue
  - mood_swings
  - circadian_disruption
  - cognitive_slowing
- Social Anxiety
  - fear_of_judgment
  - awkwardness
  - public_speaking_fear
  - avoidance
  - overthinking_interactions
  - negative_evaluation_fear
  - post_event_rumination
- Social Battery Depletion
  - exhaustion
  - irritability
  - withdrawal
  - introvert_burnout
  - brain_fog
- Social Isolation
  - loneliness
  - withdrawal
  - depression
  - fear_of_rejection
  - apathy
- Spiritual Crisis
  - loss_of_faith
  - confusion
  - existential_dread
  - alienation
  - guilt
- Success Anxiety
  - imposter_syndrome
  - fear_of_expectations
  - self_sabotage
  - pressure
  - burnout
- Technology Addiction
  - doomscrolling
  - screen_time_guilt
  - distraction
  - fomo
  - sleep_disruption
- Toxic Friendship Dynamics
  - manipulation
  - drain
  - walking_on_eggshells
  - gossip
  - competition
- Toxic Positivity Exhaustion
  - invalidation
  - suppression
  - guilt
  - burnout
  - alienation
- Transitioning to Adulthood
  - overwhelm
  - imposter_syndrome
  - nostalgia
  - fear_of_responsibility
  - loneliness
- Trust Betrayal Trauma
  - hypervigilance
  - fear_of_intimacy
  - jealousy
  - paranoia
  - emotional_walls
- Trust Issues
  - fear_of_betrayal
  - hypervigilance
  - jealousy
  - avoidance
  - testing_partners
  - suspicion_habit
  - fear_of_dependence
- Unrealistic Expectations
  - perfectionism
  - disappointment
  - pressure
  - burnout
  - comparison
- Unrequited Love
  - grief
  - obsession
  - low_self_worth
  - jealousy
  - idealization
- Work-Life Imbalance
  - burnout
  - guilt
  - relationship_strain
  - exhaustion
  - loss_of_identity
- Workplace Bullying Stress
  - anxiety
  - dread
  - low_self_esteem
  - burnout
  - paranoia

## JSON File Types

### Emotional Dataset (Per Subcategory)
- `inputs.json`
- `responses.json`
- `evaluated.json`
- `curated.json`
- `metadata.json`
- `variations.json`
- `conversation_flows.json`
- `memory_patterns.json`

### Emotional Taxonomy
- `taxonomy/categories.json`
- `taxonomy/emotions.json`
- `taxonomy/cognitive_patterns.json`
- `taxonomy/emotional_triggers.json`

### Pipeline Artifacts
- `sandhi_dataset_pipeline/raw_data/raw_posts.json`
- `sandhi_dataset_pipeline/processed_data/inputs.json`
- `sandhi_dataset_pipeline/outputs/responses.json`
- `sandhi_dataset_pipeline/outputs/evaluated.json`

### Spiritual Dataset
- `_index.json`
- Per-entry JSON files (e.g., `yoga_1_2.json`, `hitopadesa_wisdom_001.json`)

## Field Descriptions

### inputs.json (Emotional Subcategory)
Top-level type: array of objects

Fields:
- `id`: Unique input identifier.
- `emotion`: Primary emotion label.
- `surface_emotion`: Visible emotion label.
- `hidden_emotion`: Underlying emotion label.
- `emotion_intensity`: Numeric intensity (integer).
- `thought_pattern`: Thought pattern tag.
- `cognitive_distortion`: Distortion label.
- `trigger`: Trigger label.
- `user_input`: Raw user statement text.
- `age_group`: Age segment label.
- `language_style`: Style/tone label.
- `tags`: Array of string tags.
- `category`: Present in pipeline inputs; not used in subcategory inputs.
- `subcategory`: Present in pipeline inputs; not used in subcategory inputs.

### responses.json (Emotional Subcategory)
Top-level type: array of objects

Fields:
- `response_id`: Unique response identifier.
- `input_id`: Reference to an `inputs.json` id.
- `response_style`: Response style label (e.g., calming, reflective).
- `sandhi_response`: Generated response text.
- `wisdom_theme`: Theme label.
- `tone`: Tone label.
- `length`: Length label.

### evaluated.json (Emotional Subcategory)
Top-level type: array of objects

Fields:
- `response_id`: Reference to a response.
- `empathy_score`: Numeric score.
- `groundedness_score`: Numeric score.
- `genericness_score`: Numeric score.
- `emotional_safety_score`: Numeric score.
- `wisdom_depth_score`: Numeric score.
- `human_likeness_score`: Numeric score.
- `final_score`: Aggregate score.
- `approved`: Boolean approval flag.

### curated.json (Emotional Subcategory)
Top-level type: array of objects

Fields:
- `id`: Curated record id.
- `category`: Normalized category slug.
- `subcategory`: Subcategory slug.
- `emotion`: Primary emotion.
- `surface_emotion`: Surface emotion.
- `hidden_emotion`: Hidden emotion.
- `emotion_intensity`: Numeric intensity.
- `thought_pattern`: Thought pattern tag.
- `cognitive_distortion`: Distortion label.
- `trigger`: Trigger label.
- `user_input`: User statement.
- `sandhi_response`: Response text.
- `response_style`: Response style label.
- `wisdom_theme`: Theme label.
- `quality_score`: Numeric score.
- `retrieval_tags`: Array of tags.

### metadata.json (Emotional Subcategory)
Top-level type: object

Fields:
- `subcategory_id`: Subcategory identifier.
- `subcategory_name`: Subcategory name.
- `category`: Parent category name.
- `description`: Subcategory description.
- `complexity_level`: Complexity label.
- `clinical_relevance`: Clinical relevance label.
- `tags`: Array of tags.

### variations.json (Emotional Subcategory)
Top-level type: object

Fields:
- `personas`: Object mapping persona keys to example statements.
- `lexicon`: Array of lexicon terms.

### conversation_flows.json (Emotional Subcategory)
Top-level type: object

Fields:
- `flow_name`: Conversation flow name.
- `stages`: Array of stage objects with:
  - `stage`: Stage number.
  - `name`: Stage name.
  - `description`: Stage description.

### memory_patterns.json (Emotional Subcategory)
Top-level type: object

Fields:
- `cognitive_distortion`: Distortion label.
- `recurrent_themes`: Array of recurring theme tags.
- `coping_history`: Coping label.
- `episodic_markers`: Object containing:
  - `frequency`
  - `trigger_sensitivity`

### taxonomy/categories.json
Top-level type: array of objects

Fields:
- `id`: Numeric category id.
- `category`: Category name.

### taxonomy/emotions.json
Top-level type: object

Fields:
- Keys are category names.
- Values are arrays of subcategory slugs.

### taxonomy/cognitive_patterns.json
Top-level type: array of objects

Fields:
- `pattern`: Pattern name.
- `definition`: Definition text.
- `meaning`: Short meaning.
- `examples`: Array of example statements.

### taxonomy/emotional_triggers.json
Top-level type: array of objects

Fields:
- `trigger`: Trigger label.
- `surface_emotion`: Surface emotion label.
- `hidden_emotion`: Hidden emotion label.

### sandhi_dataset_pipeline/raw_data/raw_posts.json
Top-level type: array of objects

Fields:
- `subreddit`: Subreddit name.
- `title`: Post title.
- `body`: Post body.
- `score`: Post score.

### sandhi_dataset_pipeline/processed_data/inputs.json
Top-level type: array of objects

Fields:
- `emotion`
- `emotion_intensity`
- `thought_pattern`
- `user_input`
- `category`
- `subcategory`

### sandhi_dataset_pipeline/outputs/responses.json
Top-level type: array of objects

Fields:
- `response_id`
- `input_id`
- `response_style`
- `sandhi_response`
- `wisdom_theme`
- `tone`
- `length`

### sandhi_dataset_pipeline/outputs/evaluated.json
Top-level type: array of objects

Fields:
- `response_id`
- `empathy_score`
- `groundedness_score`
- `genericness_score`
- `emotional_safety_score`
- `wisdom_depth_score`
- `human_likeness_score`
- `final_score`
- `approved`

### sandhi-spritual-intelligence-dataset/_index.json
Top-level type: array of objects

Fields:
- `source`
- `book`
- `source_folder`
- `book_folder`
- `path`
- `entry_count`
- `entry_files`
- `wisdom_styles`
- `guidance_types`
- `all_emotion_tags`
- `all_problem_tags`

### Spiritual entry JSON (all collections)
Top-level type: object

Fields:
- `id`
- `source`
- `book`
- `chapter`
- `verse`
- `speaker`
- `title`
- `text`
- `modern_interpretation`
- `summary`
- `emotion_tags`
- `problem_tags`
- `guidance_type`
- `tone`
- `wisdom_style`
- `keywords`
- `life_areas`
- `intensity_level`
- `psychological_theme`
- `spiritual_theme`
- `actionable_advice`
- `embedding_ready_text`

## Example Schemas

### Emotional Input (inputs.json)
```json
{
  "id": "inp_example_001",
  "emotion": "fear",
  "surface_emotion": "fear",
  "hidden_emotion": "shame",
  "emotion_intensity": 7,
  "thought_pattern": "catastrophizing",
  "cognitive_distortion": "all_or_nothing_thinking",
  "trigger": "exam_results",
  "user_input": "...",
  "age_group": "college_student",
  "language_style": "casual",
  "tags": ["exam_results", "fear"]
}
```

### Emotional Response (responses.json)
```json
{
  "response_id": "rsp_example_001",
  "input_id": "inp_example_001",
  "response_style": "calming",
  "sandhi_response": "...",
  "wisdom_theme": "grounding",
  "tone": "calm",
  "length": "medium"
}
```

### Response Evaluation (evaluated.json)
```json
{
  "response_id": "rsp_example_001",
  "empathy_score": 9,
  "groundedness_score": 8,
  "genericness_score": 2,
  "emotional_safety_score": 10,
  "wisdom_depth_score": 9,
  "human_likeness_score": 8,
  "final_score": 8.9,
  "approved": true
}
```

### Curated Pair (curated.json)
```json
{
  "id": "curated_example_001",
  "category": "exam-anxiety",
  "subcategory": "fear_of_failing",
  "emotion": "fear",
  "surface_emotion": "fear",
  "hidden_emotion": "shame",
  "emotion_intensity": 8,
  "thought_pattern": "catastrophizing",
  "cognitive_distortion": "all_or_nothing_thinking",
  "trigger": "exam_results",
  "user_input": "...",
  "sandhi_response": "...",
  "response_style": "calming",
  "wisdom_theme": "grounding",
  "quality_score": 9.1,
  "retrieval_tags": ["exam_results", "fear"]
}
```

### Subcategory Metadata (metadata.json)
```json
{
  "subcategory_id": "SUB-EXAMPLE",
  "subcategory_name": "fear_of_failing",
  "category": "Exam Anxiety",
  "description": "...",
  "complexity_level": "medium",
  "clinical_relevance": "medium",
  "tags": ["exam_anxiety", "fear_of_failing"]
}
```

### Conversation Flow (conversation_flows.json)
```json
{
  "flow_name": "Validation to Coping",
  "stages": [
    {"stage": 1, "name": "Validation", "description": "..."},
    {"stage": 2, "name": "Reframing", "description": "..."}
  ]
}
```

### Memory Pattern (memory_patterns.json)
```json
{
  "cognitive_distortion": "overgeneralization",
  "recurrent_themes": ["comparison", "self_doubt"],
  "coping_history": "avoidant_behavior",
  "episodic_markers": {
    "frequency": "recurrent_under_high_stress",
    "trigger_sensitivity": "high_during_exams"
  }
}
```

### Spiritual Entry
```json
{
  "id": "yoga_1_2",
  "source": "Yoga Sutras",
  "book": "The Yoga Sutras of Patanjali",
  "chapter": "1",
  "verse": "2",
  "speaker": "Patanjali",
  "title": "Control of the versatile psychic nature",
  "text": "...",
  "modern_interpretation": "...",
  "summary": "...",
  "emotion_tags": ["restlessness", "discipline"],
  "problem_tags": ["lack_of_direction"],
  "guidance_type": "discipline",
  "tone": "disciplined",
  "wisdom_style": "yogic",
  "keywords": ["union", "mind_control"],
  "life_areas": ["mental_health", "spirituality"],
  "intensity_level": "transformative",
  "psychological_theme": ["mind_control"],
  "spiritual_theme": ["moksha"],
  "actionable_advice": "...",
  "embedding_ready_text": "..."
}
```

## Memory Schema Explanation
`memory_patterns.json` captures how a subcategory is remembered over time:
- **cognitive_distortion** indicates the dominant distortion pattern.
- **recurrent_themes** lists recurring topic tags tied to the memory.
- **coping_history** describes typical coping behavior.
- **episodic_markers** captures frequency and trigger sensitivity for episodic recall.

## Response Schema Explanation
Responses are split across two files:
- **responses.json** stores the response text and its tone/style metadata.
- **evaluated.json** stores numeric scoring and approval signals for response quality.

## Conversation Flow Schema Explanation
`conversation_flows.json` defines a multi-stage response plan. Each stage contains an ordered step name and descriptive guidance so downstream systems can move from validation to reframing and action.
