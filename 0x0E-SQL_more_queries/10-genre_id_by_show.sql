--DISPLAYS ALL SHOWS CONTAINED IN HBTN_0D_TV SHOWS THAT HAVE A ONE GENRE LINKED.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
