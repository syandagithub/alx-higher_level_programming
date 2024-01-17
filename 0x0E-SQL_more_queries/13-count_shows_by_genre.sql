--SHOWS ALL THE GENRES FROM THE HBTN_0D_TVSHOWS TABLE ALONG WITH THE NUMBER OF SHOWS
SELECT g.`name` AS `genre`,COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;
