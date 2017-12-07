user_id = 34
base_url = "http://student04.cse.nd.edu:51069"

window.onload = function() {
  document.getElementById('submit').onclick = function () {
    uid = document.getElementById("uid").value;
    if (uid) {
      ingredients = document.getElementById('ingredients').value.split(","); // split elements in to an array
      ingredients = ingredients.map(Function.prototype.call, String.prototype.trim) // trim whitespace
      ingredients_list = ingredients.join('&');
      clear()
      args = recipePage()
      setUp(uid, args, ingredients_list)
    }
  }

  $( "body" ).on( "click", "input[type=radio]", function() {
    vote(this.value)
  } );

  $( "body" ).on( "click", "#next_button", function() {
    clear()
    args = recipePage()
    setUp(uid, args, ingredients_list)
  } );

  $( "body" ).on( "click", "#home_button", function() {
    location.reload();
  } );
}



function clear() {
  document.getElementById('full-page').innerHTML = "";
}

function recipePage() {
  main_div = document.getElementById('full-page');
  Div.prototype = new Item();

  left = new Div();
  left.createDiv('left');

  image = new Image();
  image.createImage('recipe_image', 'http://knowledgeoverflow.com/wp-content/uploads/2013/03/food_photography_burger_by_masterdev777-d3h1ryk.jpg');

  stars_div = new Div();
  stars_div.createDiv('stars_div');

  stars = new Stars();
  stars.createStars();
  stars_div.addItem(stars);

  left.addItem(image);
  left.addItem(stars_div);

  right = new Div();
  right.createDiv('right');

  info = new Div();
  info.createDiv('info', 'text-left');

  title = new Label();
  title.createLabel("title", "recipe_title");

  ingredients = new Label("Ingredients: ");
  ingredients.createLabel("list of ingredients", "recipe_ingredients");

  rating = new Label("Rating: ");
  rating.createLabel("", "recipe_rating");

  link = new Link();
  link.createLink("View Recipe", "recipe_link", "", "btn btn-primary");

  info.addItem(title);
  info.addItem(ingredients);
  info.addItem(rating)
  info.addItem(link);

  next_div = new Div();
  next_div.createDiv("next_div");
  next = new Button();
  next.createButton("Next recipe", "next_button", "btn btn-danger");
  next_div.addItem(next);

  home = new Button();
  home.createButton("Home", "home_button", "btn btn-success");
  next_div.addItem(home);

  right.addItem(info);
  right.addItem(next_div)

  main_div.appendChild(right.item);
  main_div.appendChild(left.item);
  elements = [image, title, ingredients, rating, link];
  return elements;
}

function setUp(uid, args, ingredients_list) {
  // Get new recipe id
  var xhttp = new XMLHttpRequest();
  if (ingredients_list) {
    console.log(ingredients_list)
    url = base_url + "/recommendations/" + uid + "/" + ingredients_list;
    console.log(url)
    xhttp.open("GET", url, false);
  } else {
    xhttp.open("GET", base_url + "/recommendations/" + uid, false);
  }
  xhttp.onload = function (e) {
          recipedata = JSON.parse(xhttp.responseText);
          console.log(recipedata["recipe_id"])
          recipe_id = recipedata["recipe_id"];
  }
  xhttp.onerror = function (e) {
          console.error(xhttp.statusText);
  }
  xhttp.send(null);

  // Get the recipe info
  var xhttp2 = new XMLHttpRequest();
  xhttp2.open("GET", base_url + "/recipes/" + recipe_id, false);
  xhttp2.onload = function (e) {
    resp = JSON.parse(xhttp2.responseText);
    console.log(resp)
    args[0].changeImage(resp["recipe"]["image"]);
    args[1].setText(resp["recipe"]["name"]);
    ingredients = resp["recipe"]["ingredients"].replace(/\n/g,", ");
    console.log(ingredients)
    args[2].setText(ingredients);
    args[4].setLink(resp["recipe"]["url"]);
  }
  xhttp2.onerror = function (e) {
    console.error(xhttp2.statusText);
  }
  xhttp2.send(null);

  // Get rating
  var xhttp3 = new XMLHttpRequest();
  xhttp3.open("GET", base_url + "/ratings/"+ recipe_id, false);
  xhttp3.onload = function (e) {
          resp2 = JSON.parse(xhttp3.responseText);
          args[3].setText(resp2["rating"]);
          console.log(resp2)
  }
  xhttp3.onerror = function (e) {
          console.error(xhttp3.statusText);
  }
  xhttp3.send(null);
}

function vote(rating) {
  // Send a put to recommendations to update the user rating for the recipe
  var xhttp = new XMLHttpRequest();
  method = 'PUT',
  url = base_url + '/recommendations/' + uid;
  data = {'recipe_id': recipe_id, 'rating': rating}
  var json = JSON.stringify(data);
  xhttp.open(method, url, true);
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
        console.log(xhttp.response);
    }
  };
  xhttp.send(json);

  // Send a second PUT to save the ratings to file
  var xhttp = new XMLHttpRequest();
  method = 'PUT',
  url = base_url + '/save/';
  data = {}
  var json = JSON.stringify(data);
  xhttp.open(method, url, true);
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
        console.log(xhttp.response);
    }
  };
  xhttp.send(json);
}
