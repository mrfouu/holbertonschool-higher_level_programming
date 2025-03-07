-- This script lists all genres and the number of shows linked to each genre.
-- It displays: genre - number_of_shows.
-- Only genres with linked shows are included.
-- The results are sorted in descending order by the number of shows linked.
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
