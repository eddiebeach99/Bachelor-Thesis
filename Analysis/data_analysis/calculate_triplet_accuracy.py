import os
import re
import pandas as pd

# Script that calculates and prints the triplet accuracy between conditions.

def compare_sessions(subject_range, session1, session2):
    csv_files = [os.path.join('data', filename) for filename in os.listdir('data') if
                 'obs' in filename and filename.endswith('.csv')]

    # This depends strongly on how the files were named again. Here Observers are identified by the expression that comes
    # after 'obs'
    filtered_csv_files = []


    for filename in csv_files:
        subject_num = int(re.findall(r'obs(\d+)', filename)[0])
        if subject_num in subject_range:
            filtered_csv_files.append(filename)

    file_groups = {}
    for filename in filtered_csv_files:
        subject_num = re.findall(r'obs(\d+)', filename)[0]

        if subject_num not in file_groups:
            file_groups[subject_num] = []
        file_groups[subject_num].append(filename)

    percent_matchings = []




    for subject_num, filenames in file_groups.items():
        session_filenames = []
        for filename in filenames:
            session_num = int(re.findall(r'sess(\d+)', filename)[0])
            if session_num == session1 or session_num == session2:
                session_filenames.append(filename)

        df1 = pd.read_csv(session_filenames[0])
        df2 = pd.read_csv(session_filenames[1])

        # Here I merged the data so we can more easily calculate triplet accuracy
        merged = pd.merge(df1, df2, on=['index_left', 'index_middle', 'index_right'])

        num_rows = len(merged)
        num_matching = (merged['BB_Trial.resp_x'] == merged['BB_Trial.resp_y']).sum()
        percent_matching = (num_matching/num_rows) * 100
        percent_matchings.append(percent_matching)
        print(f"subject {subject_num} with sessions{session1} and {session2} have {percent_matching:.2f} matching percent.")

    return

results1 = compare_sessions(range(1, 5), 1, 3)
print(results1)

results2 = compare_sessions(range(1,5), 2, 4)
print(results2)
