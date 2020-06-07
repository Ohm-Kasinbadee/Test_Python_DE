Question 1: Data Extraction

Instructions:
1. Extract "loss circulation" value from the activity memo of the given dataset
2. Name the column containing the extracted values "LOSS_CIRCULATION"
3. Concatenate the new column to the dataset and save to a csv file named "loss-circulation-transformed.csv"

Extraction Logics:
- Locate the keyword "loss" in "DM_ACTIVITY.activity_memo" column.
- The numeric in (m3) unit that follows are the value to be extracted.
- In case of absence, loss circulation value should defalut to zero.

======================

Question 2: Data Profiling

Answer the following questions
- What are the some basic statistics (avg, var, max, min, %missing) of loss circulation?
- Using visualization tools of choice, plot the distribution of loss circulation.
- What are the top 3 activity codes from which loss circulation occurs the most?