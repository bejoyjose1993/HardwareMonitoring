import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MetricsModel } from '../models/metricsModel';


@Injectable({
  providedIn: 'root'
})
export class MetricsService {
  private apiUrl = 'http://localhost:8000/metrics';

  constructor(private http: HttpClient) { }

  getMetrics(): Observable<MetricsModel> {
    return this.http.get<MetricsModel>(this.apiUrl);
  }
}
