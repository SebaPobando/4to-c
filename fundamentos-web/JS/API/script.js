async function getCoderData() {
    var response = await fetch("https://api.github.com/users/dev-marisa");
    var coderData = await response.json();
    console.log(coderData);
}

getCoderData();