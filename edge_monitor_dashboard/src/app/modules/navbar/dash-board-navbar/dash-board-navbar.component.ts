import { Component } from '@angular/core';
import { StorageService } from '../../../auth/services/storage/storage.service';
import { Router, RouterModule  } from '@angular/router';
import { Subscription } from 'rxjs';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'dash_board_navbar',
  standalone: true,
  imports: [CommonModule, RouterModule ],
  templateUrl: './dash-board-navbar.component.html',
  styleUrls: ['./dash-board-navbar.component.scss']
})
export class DashBordNavbarComponent {
  isCustomerLoggedIn:boolean = true;
  showDropdown = false;
  menuOpen = false;
  private authSubscription!: Subscription;
  constructor(private router: Router){}

  ngOnInit(){
    this.authSubscription = StorageService.isLoggedIn$.subscribe(
      (status) => {
        this.isCustomerLoggedIn = status;
      }
    );
  }


  ngOnDestroy() {
    if (this.authSubscription) {
      this.authSubscription.unsubscribe();
    }
  }


  logout(){
    StorageService.logout();
    this.isCustomerLoggedIn = StorageService.isCustomerLoggedIn();
    this.router.navigateByUrl("/login");
  }

  toggleMenu() {
    this.menuOpen = !this.menuOpen;
  }

}
