import {Card} from "antd";

function CryptocurrencyCard(props) {
  const { currency } = props
  const price = Math.round(currency.quote.USD.price)
  const capitalization = Math.round(currency.quote.USD.market_cap) / 1_000_000
  const percent_change = Math.round(parseFloat(currency.quote.USD.percent_change_24h)*100) / 100

  return (
      <div>
        <Card
          title={
            <div className="flex items-center gap-3">
              <img src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}/>
              <span>{currency.name}</span>
            </div>
          }
          style={{
            width: 300,
          }}
        >
          <p>Current price: {price}$</p>
          <p>Percent change: {percent_change}%</p>
          <p>Capitalization: {capitalization}M $</p>
        </Card>
      </div>
  )
}

export default CryptocurrencyCard