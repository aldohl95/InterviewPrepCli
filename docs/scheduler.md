# Spaced Repetition Scheduling Algorithm

## Purpose
Automatically determine when a user should review a problem next, based on how 
difficult they found it and whether they needed help.

## Design Principles
- Simple over sophisticated: piecewise function, not SM-2
- Personal difficulty is the primary signal
- First reviews use gentler intervals; subsequent reviews are more aggressive
- Errors on the side of over-reviewing rather than forgetting

## Algorithm

### Determining review number
A review is considered a "first review" if no prior `Problem` records exist with 
the same `problem_name`. Otherwise it is a "subsequent review."

### First review intervals
| Personal Difficulty | Next review in |
|---|---|
| 6-10 (struggled) | 1 day |
| 1-5 (comfortable) | 3 days |

### Subsequent review intervals
| Condition | Next review in |
|---|---|
| needed_help OR personal_difficulty >= 8 | 1 day |
| personal_difficulty 6-7 | 3 days |
| personal_difficulty 4-5 | 7 days |
| personal_difficulty 2-3 | 14 days |
| personal_difficulty 1 | 30 days |

## Known Limitations
- `problem_name` is used as a de facto identifier for looking up prior attempts. 
  Two different problems sharing a name would be treated as the same problem.
- No support for manual override of scheduled dates yet.

### Handling Review Overload
The algorithm's tight 1-day interval for hard problems can create daily review 
backlogs when a user struggles with multiple problems in the same session. This is 
intentional the algorithm's job is to signal what needs review, not to manage 
daily volume. Load management is handled by the Daily Study Planner (Feature 4), 
which caps daily reviews and prioritizes by overdue-ness.

## Future Considerations
- Migration to SM-2 or FSRS if the tool scales beyond interview prep
- Splitting `Problem` and `Attempt` into separate models for cleaner identity handling