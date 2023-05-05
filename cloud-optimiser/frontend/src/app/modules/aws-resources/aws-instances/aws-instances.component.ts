import { Component, OnInit, ViewChild, Input, OnChanges } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
//import { DeletedInstances } from '../../../models/Deleted-Resources.model';
//import { DeletedResourcesService } from 'src/app/services/deleted-resources.service';
import { ActivatedRoute } from '@angular/router';

@Component({
selector: 'app-aws-instances',
templateUrl: './aws-instances.component.html',
styleUrls: ['./aws-instances.component.scss']
})
export class AwsInstancesComponent implements OnInit,OnChanges {
	panelOpenState=false;
	expandPanel = false;
	public displayedColumns1: string[] = ['id','name','owner','purpose','state','age','dnd','instance_type','public_ip','region'];
	public dataSource1= new MatTableDataSource<any>();
constructor() {}
ngOnInit(): void{
}
ngOnChanges(): void{}
}
