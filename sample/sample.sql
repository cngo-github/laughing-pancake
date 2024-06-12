SELECT DISTINCT ON (image_id) image_id, score, weak_label
FROM
(
  (
    SELECT image_id, score, 1 as weak_label
    FROM
    (
      SELECT image_id, score, ROW_NUMBER() OVER (ORDER BY score DESC) AS rownum
      FROM unlabeled_image_predictions
    ) AS positives
    WHERE (
      	positives.rownum % 3 = 1
    )
    LIMIT 10000
  )
  UNION
  (
    SELECT image_id, score, 0 as weak_label
    FROM
    (
      SELECT image_id, score, ROW_NUMBER() OVER (ORDER BY score ASC) AS rownum
      FROM unlabeled_image_predictions
    ) AS negatives
    WHERE (
      	negatives.rownum % 3 = 1
    )
    LIMIT 10000
  )
) as samples
ORDER BY image_id, weak_label ASC
