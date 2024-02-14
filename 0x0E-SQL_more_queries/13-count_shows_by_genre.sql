-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Import the database dump from hbtn_0d_tvshows
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg 
ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
