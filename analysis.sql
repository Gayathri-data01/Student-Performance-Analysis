-- Create table
CREATE TABLE students (
    gender VARCHAR(10),
    math_score INT,
    reading_score INT,
    writing_score INT
);

-- Insert data
INSERT INTO students VALUES
('male',78,72,70),
('female',90,88,95),
('male',60,65,63),
('female',85,80,82),
('male',50,55,58),
('female',95,92,96),
('male',70,68,72),
('female',88,85,90);

-- Average scores
SELECT 
AVG(math_score) AS avg_math,
AVG(reading_score) AS avg_reading,
AVG(writing_score) AS avg_writing
FROM students;

-- Top performers
SELECT *, 
(math_score + reading_score + writing_score) AS total
FROM students
ORDER BY total DESC
LIMIT 5;

-- Gender-wise performance
SELECT gender,
AVG(math_score),
AVG(reading_score),
AVG(writing_score)
FROM students
GROUP BY gender;
