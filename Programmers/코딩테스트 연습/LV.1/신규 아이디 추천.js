const solution = (new_id) => {
    const answer = new_id
        .toLowerCase()
        .replace(/[^\w-._]+/g,'')
        .replace(/[\.]{2,}/g,'.')
        .replace(/^\./, '')
        .replace(/\.$/,'')
        .replace(/^$/, 'a')
        .slice(0, 15).replace(/\.$/, '');
    
    const len = answer.length
    
    const result = (len <= 2) ? answer.padEnd(3, answer[len-1])
    : answer ;
    
    return result;
}