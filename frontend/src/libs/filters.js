const limitTo = function(str, len){
    if(!str) return;
    return str.substr(0, len)
}

export { limitTo }