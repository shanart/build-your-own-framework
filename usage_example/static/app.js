$(document).ready(function () {
  const loginForm = $("#login-form");
  let token = localStorage.getItem("token");

  if (token !== null) {
    loginForm.hide();
  } else {
    loginForm.show();
  }

  loginForm.on("submit", function (event) {
    event.preventDefault();
    $.ajax({
      type: 'POST',
      url: "/login",
    }).done(function (data) {
      token = data["token"];
      localStorage.setItem("token", token);
      $("#login-form").hide();
    }).fail(function () {
      console.log("Failed to login!");
    });
  });

  $("#create-form").on("submit", function (e) {
    e.preventDefault();

    let name = $("#name").val();
    let author = $("#author").val();

    $.ajax({
      type: 'POST',
      url: "/books",
      headers: {
        "Authorization": "Token: " + token
      },
      data: {"name": name, "author": author},
      statusCode: {
        401: function () {
          alert('Authorize First!');
        }
      }
    }).done(function (data) {
      console.log(data);
    }).fail(function () {
      console.log("Failed to create!");
    })
  });

  $(".delete-button").on("click", function (e) {
    let r = confirm("Sure you want to delete this book?");
    let bookId = $(this).data("id");

    if (r === true) {
      $.ajax({
        type: 'DELETE',
        url: "/books/" + bookId,
        headers: {
          "Authorization": "Token: " + token
        },
        statusCode: {
          401: function () {
            alert('Authorize First!');
          }
        }
    }).done(function (data) {
        console.log(data);
      }).fail(function () {
        console.log("Failed to delete!");
      });
    } else {
      console.log("You pressed Cancel!");
    }
  })
});