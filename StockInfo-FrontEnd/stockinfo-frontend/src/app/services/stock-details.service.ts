import { Injectable } from '@angular/core';

import { Stock } from '../interfaces/stock';

import { Observable } from 'rxjs/Observable';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Injectable()
export class StockDetailService {
  constructor(
    private http: HttpClient,
  ) { }

  private stockDetailUrl = 'https://www.alphavantage.co/query?function='

  constructUrlString(time_series, symbol, apikey){
    this.stockDetailUrl = this.stockDetailUrl + time_series + '&';
    this.stockDetailUrl = this.stockDetailUrl + 'symbol=' + symbol + '&';
    this.stockDetailUrl = this.stockDetailUrl + 'apikey=' + apikey

  }

  getStockDetails(): Observable<Stock> {
    return this.http.get<Stock>(this.stockDetailUrl);
  }

}
