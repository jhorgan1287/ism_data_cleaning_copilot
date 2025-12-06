# Reflection

## What Copilot Generated

Copilot helped create a lot of the starting structure of my project, especially in the early steps of loading and cleaning the data. Many of the function outlines and basic code blocks came from its suggestions after I wrote comments like `# clean the sales dataframe` or started typing part of a function. Once it recognized the pattern, it filled in loops, Pandas operations, and formatting for me. It was useful for getting the project moving, especially when I wasn’t sure how to begin certain sections.

## What I Modified

Even though Copilot gave me a solid starting point, I still had to make a lot of changes to make the code work properly and meet the assignment requirements. I renamed several variables to make them clearer and easier to follow, and I fixed parts of the logic where Copilot guessed incorrectly about what my dataset looked like. Sometimes it included steps that didn’t apply to my file or tried to drop columns that didn’t exist. I reorganized the cleaning process so that everything happened in the right order and added things like `.str.title()` to fix formatting issues. These edits were important because they made my code more accurate, readable, and aligned with what the assignment was actually asking for.

## What I Learned

Throughout this project, I learned a lot about how data cleaning works in Python and how to use Copilot responsibly as a tool. Pandas makes it pretty easy to clean and organize data once you understand the basic functions, but I also realized how important it is to double-check everything—AI doesn’t always know exactly what my dataset needs. For example, Copilot didn’t automatically convert names to proper case, which caused an autograder error, so I added `.str.title()` myself. This showed me that Copilot is great for generating ideas and speeding things up, but I still have to think critically about the code and make sure it truly fits the assignment. Overall, the project helped me become more confident with data cleaning and with editing AI-generated code to meet academic expectations.
