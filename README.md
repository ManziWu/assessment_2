# Preliminary Review of Intellectual Property License Agreement

## Deployed Application
The application is deployed at the following URL: 

## How to Use
1.Upload your intellectual property license agreement in PDF, DOCX, or plain text format, or paste the content directly into the input field.
2.Click the Check button for each key clause to generate evaluations and explanations.
3.Once all clauses are reviewed, click Overall Assessment to see whether the agreement is complete, incomplete, or uncertain
## Test Case
### Test Case 1
Objective: Verify that the tool correctly identifies a complete agreement.
Input:

Method 1: File Upload
Upload a PDF or DOCX file containing all six key clauses:

Scope of Authorization: Clearly defined.
Authorization Duration: Start and end dates specified.
Usage Restrictions: Explicitly stated.
Payment Terms: Detailed fees and payment schedule.
IP Ownership: Properly assigned.
Termination Terms: Clear and specific.
Method 2: Plain Text Input
Paste the entire content of the complete agreement into the plain text input field.

Expected Output:

All clauses are marked "Yes" with appropriate explanations.
Overall Assessment: "The agreement is complete."

### Test Case2:
Objective: Test the tool’s ability to handle agreements with missing or unclear clauses.
Input:

Method 1: File Upload
Upload a PDF or DOCX file missing the following clauses:

Usage Restrictions
Termination Terms
Method 2: Plain Text Input
Paste agreement content missing the "Usage Restrictions" and "Termination Terms" clauses into the plain text input field.

Expected Output:

"Usage Restrictions" and "Termination Terms" are marked "No," with explanations indicating their absence.
Overall Assessment: "The agreement is incomplete."

### Test Case3:
Objective: Verify that the tool correctly handles partially completed agreements with some vague clauses.
Input:

Method 1: File Upload
Upload a PDF or DOCX file where some clauses are vague, such as:

Scope of Authorization: Defined, but lacks specific limitations.
Payment Terms: Mentioned, but details (e.g., amounts, schedules) are missing.
Method 2: Plain Text Input
Paste agreement content into the plain text field where:

"Scope of Authorization" clause does not include usage limits.
"Payment Terms" are referenced without specific amounts.

Expected Output:

"Scope of Authorization" is marked "No", with an explanation: "The scope lacks specific limitations."
"Payment Terms" is marked "No", with an explanation: "Payment details are missing."
Other well-defined clauses are marked "Yes" with appropriate explanations.
Overall Assessment: "The agreement is incomplete."

## Test Artifacts
To run the test case, the following artefact is provided in the repository:

sample_case3.2 Lynch v Lynch (1991) 14 MVR 512.pdf: This PDF file is required for testing the file upload functionality. Please upload this file in Step 1 when using the application.

## Setup

Setup your repository by following these steps. In the terminal:

> conda create -n . python=3.12

> conda init

--> close and reopen terminal

> conda activate .

> conda install -c conda-forge sqlite

> pip3 install -r requirements.txt

--> run `python -m streamlit run Home.py` to confirm everything is working

> create .env file and add OPENAI_API_KEY="" with your API key

If you can't see the following already:

> create a .streamlit folder and inside this folder create a file named config.toml

> inside of the config.toml file add the following text:

```
[server]
enableXsrfProtection = false
enableCORS = false
```

## Save Your Code

> git add -A

> git commit -m "update"

> git push

Once this is done you can delete the codespaces to free up new space.

## Reopen Terminal

If you don't see the (/opt/conda/envs), use:

`conda activate .`