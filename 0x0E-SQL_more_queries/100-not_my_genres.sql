-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- Import the database dump from hbtn_0d_tvshows
SELECT DISTINCT tg.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
INNER JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE tg.id NOT IN (
  SELECT tg.id
  FROM tv_genres AS tg
  INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
  INNER JOIN tv_shows AS ts ON tsg.show_id = ts.id
  WHERE ts.title = "Dexter"
)
ORDER BY tg.name;
