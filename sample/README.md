Made with PostgresSQL v12 on [DB-Fiddle](https://www.db-fiddle.com/).

# Notes

The **sample.sql** query selects 10K positive and 10K negative samples and aggregates them. The positive samples have a _weak_label_ of 1, while the negative ones have a _weak_label_ of 0. It also ensures no duplicate entries, based on _image_id_, are returned. In cases where an _image_id_ has both negative and positive samples, the negative one is chosen. So, if there are not more than 10,000 records in the database, both positive and negative sampling will return all rows. So, all entries returned will have a _weak_label_ of 0. Finally, the combined entries are ordered by _image_id_.
