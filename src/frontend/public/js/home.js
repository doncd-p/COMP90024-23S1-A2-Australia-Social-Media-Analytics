var count1 = 0;
var count2 = 0;
var typingtext1 = "<h1>TRAVEL IS THE ONLY THING</h1>";
var typingtext2 = "WELCOME TO MELBOURNE";

var myBlock1 = document.getElementById("info1");
var myBlock2 = document.getElementById("info2");
// 这里是将字符串的文本解析为HTML
function type() {
  if (count1 <= typingtext1.length) {
    myBlock1.innerHTML = typingtext1.substring(0, count1);
    count1++;
  } else {
    window.clearInterval(intervalID);
  }
}
function type2() {
  if (count2 <= typingtext2.length) {
    myBlock2.innerHTML = typingtext2.substring(0, count2);
    count2++;
  } else {
    window.clearInterval(intervalID);
  }
}

// 这里定义速度，单位为毫秒
var intervalID = window.setInterval(type, 45);
var intervalID = window.setInterval(type2, 65);
