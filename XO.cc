const reset= ()=>{
    setSquares(Array(9).fill(null));
    setWinner(null)
    setCurrentPlayer(Math.round(Math.random()*1) === 1 ? 'Med' : 'Amine');

    
}
const setSquareValue=(index: number)=>{
    const newData = squares.map((val,i)=>{
        if (i==index){
            return currentPlayer;

        }
        return val;
    })
    setSquares(newData);
    setCurrentPlayer(currentPlayer == 'Med' ? 'Amine' : 'Med')
}
const calculWinner=(squares:    Player[]){
    const lines = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for( let i=0;i< lines.length;i++){
        const [a,b,c] = lines[i]
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c])
        return squares[a]
    }
}
return null;