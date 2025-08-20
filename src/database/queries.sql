SELECT * from ipl_matches;


-- Top 10 batsmen by total runs in ODI matches
SELECT player_of_match, COUNT(*) AS awards
FROM odi_matches
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 10;

-- Leading wicket-takers in T20 matches (approx, based on player_of_match)
SELECT player_of_match, COUNT(*) AS awards
FROM t20_matches
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 10;

-- Team with the highest win percentage in Test cricket
SELECT winner, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM test_matches) AS win_percentage
FROM test_matches
GROUP BY winner
ORDER BY win_percentage DESC
LIMIT 5;

-- Total centuries across all formats (using player_of_match as proxy)
SELECT match_type, COUNT(player_of_match) AS total_awards
FROM (
    SELECT 'Test' AS match_type, player_of_match FROM test_matches
    UNION ALL
    SELECT 'ODI', player_of_match FROM odi_matches
    UNION ALL
    SELECT 'T20', player_of_match FROM t20_matches
    UNION ALL
    SELECT 'IPL', player_of_match FROM ipl_matches
) t
GROUP BY match_type;

-- Matches with the narrowest margin of victory (if available)
SELECT * FROM odi_matches WHERE winner != '' LIMIT 5;
