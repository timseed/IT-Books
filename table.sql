.output latest.html
select "<html><head>Latest E-Books</head><h1>Books</h1><table>";
.mode html
.headers on
select * from ebooks order by date_found;
.headers off
.mode column
select "</table></html>";
.exit
