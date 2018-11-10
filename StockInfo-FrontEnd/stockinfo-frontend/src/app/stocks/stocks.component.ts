import { Component, OnInit } from '@angular/core';
import { Stock } from '../interfaces/stock';
import { StocksService } from '../services/stocks.service';
import { StockDetailService } from '../services/stock-details.service';

@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.css'],
  providers: [StocksService, StockDetailService]
})
export class StocksComponent implements OnInit {

  selectedStock : Stock;
  stocks : Stock[];
  onStockClick(stock: Stock){
    // get the API details here from the alphaadvantage API here
    this.stockDetailService.constructUrlString('TIME_SERIES_DAILY', stock.symbol, 'SQ19E6KPE7TC636A') // hide api key
    this.stockDetailService.getStockDetails().subscribe(details => {
      console.log(details)});
  }

  getStocks(): void {
    this.stockService.getStocks().subscribe(stocks => this.stocks = stocks);
  }
  constructor(private stockService: StocksService, private stockDetailService: StockDetailService) {

  }

  ngOnInit() {
    this.getStocks();

  }

}
