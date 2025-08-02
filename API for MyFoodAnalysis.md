What are we trying to do:


1. Create a website where you can send a search item and return the food names in the results


Web site

HTML - 

<html>
<h1>My Food Anlysis</h1>
</html>

To run this 

python -m http.server



API

http://localhost:8000/api/search?keyword=campbells

Campbell's Condensed 25% Less Sodium Chicken Noodle Soup, 10.75 Ounce Can      
Campbell's Chunky Soup, Healthy Request Chicken Noodle Soup, 18.8 Ounce Can   

http://localhost:8000/api/search?keyword=redbull

Energy drink (Red Bull) 
Energy drink, sugar-free (Red Bull)

1. Read the parameter from the url
2. Construct a SQL statement using the parameter's value
3. Execute the SQL on the database, and return the display results to the user






