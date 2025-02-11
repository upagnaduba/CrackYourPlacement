select s.student_id, s.student_name, t.subject_name, count(e.subject_name) attended_exams from students s cross join subjects t
left join Examinations e on
e.student_id = s.student_id  and
e.subject_name = t.subject_name
group by s.student_name, t.subject_name
order by s.student_id, t.subject_name;