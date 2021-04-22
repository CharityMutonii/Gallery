function myFunction() {
    var copyText = document.getElementById("input");
    copyText.select();
    copyText.setSelectionRange(0, 99999); 
    document.execCommand("copy");
    alert("Copied the text: " + copyText.value);
  }