SELECT
    st.student_id,
    st.student_name,
    sub.subject_name,
    COALESCE(COUNT(st.student_id), 0) AS attended_exams
FROM students st
CROSS JOIN subjects sub
LEFT JOIN examinations ex ON ex.student_id = st.student_id AND ex.subject_name = sub.subject_name
GROUP BY st.student_id, st.student_name, sub.subject_name
ORDER BY st.student_id, sub.subject_name;