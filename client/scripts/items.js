// Create item object
function Item() {
  this.addToDocument = function() {
    document.body.appendChild(this.item);
  };
}

// Create div object
function Div() {
  this.createDiv = function(id, classes = "") {
    this.item = document.createElement("div");
    this.item.setAttribute("id", id);
    this.item.setAttribute("class", id + " " + classes);
  };
  this.addItem = function(object) {
    this.item.appendChild(object.item);
  };
}

// Create label object
function Label(static_text = "") {
  this.static_text = static_text;
  this.createLabel = function(text, id) {
    this.item = document.createElement("p");
    this.item.setAttribute("id", id);
    var text = document.createTextNode(this.static_text + text);
    this.item.appendChild(text);
  };
  this.setText = function(text) {
    this.item.innerHTML = this.static_text + text;
  };
}

// Create link object
function Link() {
  this.createLink = function(text, id, src, classes = "") {
    this.item = document.createElement("a");
    this.item.setAttribute("id", id);
    var text = document.createTextNode(text);
    this.item.appendChild(text);
    this.item.setAttribute('href', src);
    this.item.setAttribute('class', classes)
  };
  this.setLink = function(src) {
    this.item.setAttribute('href', src);
  };
}

// Create button object
function Button() {
  this.createButton = function(text, id, classes = "btn") {
    this.item = document.createElement("button");
    this.item.setAttribute("id", id);
    var text = document.createTextNode(text);
    this.item.appendChild(text);
    this.item.setAttribute("class", classes);
  };
  this.addClickEventHandler = function(handler, args) {
    this.item.onmouseup = function () {
      handler(args);
    };
  };
}

// Create dropdown object
function Dropdown() {
    this.createDropdown = function(dict, id, selected) {
      this.item = document.createElement("select");
      this.item.setAttribute("id", id);
      for (var key in dict) {
        var opt = document.createElement("option");
        opt.value = key;
        opt.innerHTML = dict[key];
        this.item.appendChild(opt);
      }
      this.item.value = selected;

    };
    this.getSelected = function() {
      return this.item.value;
    };
}

// Create image object
function Image() {
  this.createImage = function(id, url) {
    this.item = document.createElement("div");
    this.item.setAttribute("id", id);
    this.item.style.backgroundImage = "url(" + url + ")";
  };
  this.changeImage = function(url) {
    this.item.style.backgroundImage = "url(" + url + ")";
  };
}

// Create star rating object
function Stars() {
  this.createStars = function(classes = "rating-form") {
    this.item = document.createElement("form");
    this.item.setAttribute("class", classes);
    var item = document.createElement("div");
    item.setAttribute("class", "form-item");
    for (var i = 5; i >= 1; i--) {
      var input = document.createElement("input");
      input.setAttribute("type", "radio");
      input.setAttribute("id", "rating-"+i);
      input.setAttribute("name", "rating");
      input.setAttribute("value", i);
      var label = document.createElement("label");
      label.setAttribute("for", "rating-"+i);
      label.setAttribute("data-value", i);
      label.setAttribute("title", "text");
      var star = document.createElement("span");
      star.setAttribute("class", "rating-star");
      var filled = document.createElement("i");
      filled.setAttribute("class", "fa fa-star");
      var unfilled = document.createElement("i");
      unfilled.setAttribute("class", "fa fa-star-o");
      star.appendChild(filled);
      star.appendChild(unfilled);
      label.appendChild(star);
      item.appendChild(input);
      item.appendChild(label);
    }
    this.item.appendChild(item);
  }
}
