function user_choice(choice){
    const Http = new XMLHttpRequest();
    const url='http://localhost:5000/rps' + choice;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
      }
}