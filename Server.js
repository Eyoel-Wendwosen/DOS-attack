var express = require('express');
var bodyParser = require('body-parser')
var app = express()


app.get('/calculateRandom', (req, res)=>{
    let temp1 = req.query["num1"]
    let temp2 = req.query["num2"]

    let result = temp1 * temp2
    result *= result/temp2 * result / temp1
    result *= (result + temp2 ) * (temp2 - result * 4)

    res.status(200).send(result.toString())

})

app.listen(4300);