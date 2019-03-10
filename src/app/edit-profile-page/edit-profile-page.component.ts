import { Component, OnInit } from '@angular/core';

// Api lib
import { HttpClient } from "@angular/common/http";
import { ApiInterfaceService } from "../services/api-interface.service";

// Token lib
import { TokenStorageService } from "../services/token-storage.service";

// Routing
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-edit-profile-page',
  templateUrl: './edit-profile-page.component.html',
  styleUrls: ['./edit-profile-page.component.sass']
})
export class EditProfilePageComponent implements OnInit {

  /**
  {
	"id": 5,
	"user": {
		"id": 6,
		"username": "RatBoi",
		"first_name": "",
		"last_name": "",
		"email": ""
	},
	"phone_number": "",
	"bio": "",
	"isVendor": false
}**/
  public profile: any = null;
  public userToken: string;

  constructor(private api: ApiInterfaceService, private tokenStore: TokenStorageService,private router: Router, private route: ActivatedRoute) {

  }

  //updates the profile on the server
  updateProfile() {
    console.log("updating profile");
    this.api.updateProfile(this.userToken, this.profile)
      .subscribe({
        next: data => {
          console.log("updated")
          console.log("data")
        },
        complete: () => {
          this.router.navigate(['/profile'])
        }
      })
  }

  //Gets the profile on init
  ngOnInit() {
    //gets the user token
    console.log("TOKEN");
    this.tokenStore.getToken().subscribe(data => {
      let token = data as string;
      if (data !== null) {
        this.userToken = token;
        this.getProfile();
      }
    });
  }

  //Gets the logged in profile from the server
  getProfile() {
    this.api.getProfile(this.userToken).subscribe(profile => {
      this.profile = profile;
      console.log(this.profile);
    })
  }

  //TODO redirect to login on fail

}