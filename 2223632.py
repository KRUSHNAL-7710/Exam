import pandas as pd

attendance_data={
    'student_id': [101,101,101,101,101,102,102,102,102,103,103,103,103,103,104,104,104,104,104,],
    'attendance_date':pd.date_range('01-03-2024','02-03-2024','03-03-2024','04-03-2024','05-03-2024','02-03-2024','03-03-2024','04-03-2024','05-03-2024',
                                    '05-03-2024','06-03-2024','07-03-2024','08-03-2024','09-03-2024','01-03-2024','02-03-2024','03-03-2024','04-03-2024','05-03-2024'),
    'status':['Absent','Absent','Absent','Absent','Present','Absent','Absent','Absent','Absent','Absent','Absent','Absent','Absent','Absent','Present','Present','Absent','Present','Present',]
}

students_data={
    'student_id':[101,102,103,104],
    'student_name':['Alice Johnson','Bob Smith','Charlie Brown','David Lee','Eva White'],
    'parent_email':['alice_parent@example.com','bob_parent@example.com','invalid_email.com','invalid_email.com','eva_white@example.com']
}

attendance_df=pd.DataFrame(attendance_data)
students_df=pd.DataFrame(students_data)

def find_absent_students(attendance_df):
     attendance_df['attendance_date']=pd.to_datetime(attendance_df['attendance_date'])
     attendance_df=attendance_df.sort_values(by=['student_id','attendance_date'])
     
  absence_streaks=attendance_df[attendance_df['absent']].groupby(['student_id', 'group']).agg(
        absence_start_date=('attendance_date','min'),
        absence_end_date=('attendance_date','max'),
        total_absent_days=('attendance_date','count'))

     absence_streaks=absence_streaks[absence_streaks['total_absent_days']>3]

