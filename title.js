// 通过js在文章主页获取每一章的链接
let container = document.getElementsByClassName('panel-body')[1].children[0].children;
let count = container.length;
let arr = [];
for(let i=0; i<count; i++){
    link = container[i].href;
    arr[i] = link;
}
console.log(arr);