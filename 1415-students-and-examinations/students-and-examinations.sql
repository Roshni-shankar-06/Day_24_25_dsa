# Write your MySQL query statement below
SELECT
  Students.student_id,
  Students.student_name,
  Subjects.subject_name,
  COUNT(Examinations.student_id) AS attended_exams
