# Employee Status Classification

This project classifies employees into different categories based on their years of experience, performance score, and wether they are team players.

## Inputs
- experience_years (numeric): The number of years the employee has worked.
- performance_score (int): The employee's performance score (0-100).
- is_team_player (boolean): Whether the employee is a team player (True/False).

## Outputs
- "invalid": When experience_years < 0 or performance_score is not between 0 and 100.
- "senior candidate": When experience_years >= 5, performance_score >= 80, and is_team_player is True.
- "strong candidate": When experience_years >= 3 or performance_score >= 70, and is_team_player is True.
- "average candidate": For all other valid input combinations.

## Examples
Input: (6, 85, True)  
Output: "senior candidate"

Input: (4, 75, True)  
Output: "strong candidate"

Input: (2, 75, True)  
Output: "average candidate"

Input: (7, 90, False)  
Output: "average candidate"

Input: (-1, 80, True)  
Output: "invalid"
