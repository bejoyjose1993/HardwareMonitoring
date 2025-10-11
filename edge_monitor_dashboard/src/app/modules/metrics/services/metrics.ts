import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MetricsModel } from '../models/metricsModel';
import { environment } from '../../../../environments/environment';
export const FP_BASE_URL = environment.fpApiUrl;

@Injectable({
  providedIn: 'root'
})
export class MetricsService {
  private apiUrl = `${FP_BASE_URL}/metrics`;

  constructor(private http: HttpClient) { }

  getMetrics(): Observable<MetricsModel> {
    return this.http.get<MetricsModel>(this.apiUrl);
  }
}
