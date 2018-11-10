import { Injectable } from '@angular/core';

import { Stock } from '../interfaces/stock';

import { Observable } from 'rxjs/Observable';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Injectable()
export class StocksService {
  constructor(
    private http: HttpClient,
  ) { }

  private stocksUrl = 'http://127.0.0.1:8000/api/stocks/'

  getStocks(): Observable<Stock[]> {
    return this.http.get<Stock[]>(this.stocksUrl);
  }

}
