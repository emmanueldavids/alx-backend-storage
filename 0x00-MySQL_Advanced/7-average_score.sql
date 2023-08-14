-- a SQL script that creates a stored procedure ComputeAverageScoreForUser 
-- That computes and store the average score for a student. Note: An average score can be a decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    SELECT SUM(score), COUNT(*) INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;

    IF total_projects > 0 THEN
        UPDATE users
        SET average_score = total_score / total_projects
        WHERE id = user_id;
    END IF;
END;
//

DELIMITER ;
