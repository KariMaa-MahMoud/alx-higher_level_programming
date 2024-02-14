-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- import hbtn_0d_tvshows to your MySQL server
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
