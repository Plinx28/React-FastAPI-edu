import {Card} from "antd";

function CryptocurrencyCard(props) {
  const { currency } = props
  const price = Math.round(parseFloat(currency.quote.USD.price*1_000_000)) / 1_000_000
  const capitalization = Math.round(currency.quote.USD.market_cap) / 1_000_000
  const percent_change = Math.round(parseFloat(currency.quote.USD.percent_change_24h)*100) / 100

  const changeColor = percent_change >= 0 ? "text-green-500" : "text-red-500"

  return (
      <div>
          <Card
              title={
                  <div className="flex items-center gap-3 resize-y ">
                      <img className="w-10 max-h-full m-2"
                           alt={currency.name}
                           src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}/>
                      <span className="text-2xl">{currency.name}</span>
                  </div>
              }
              style={{
                  width: 350,
              }}
          >
              <p className="text-lg">Current price: {price}$</p>
              <span className="text-lg">Percent change: </span>
              <span className={`font-bold text-lg ${changeColor}`}>{percent_change}%</span>
              <p className="text-lg">Capitalization: {capitalization}M $</p>
          </Card>
      </div>
  )
}

export default CryptocurrencyCard