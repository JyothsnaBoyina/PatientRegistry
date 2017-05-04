var myApp = angular.module("myModule", []);

var config = {
            headers : {
                "Content-Type": "application/json; charset = utf-8;"
            }
        };

myApp.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);

    
myApp.controller("myController", function ($scope,$http,$filter)
    {
        $scope.flag=true;
        $scope.age=0;

        $scope.setflag=function()
        {                  
            $scope.flag=!($scope.flag);
            $http.get('/patients/api/patient/?format=json').then(function(response){$scope.patients=response.data;});

        };
        
        $scope.gend = {
         "type": "select",
          "name": "gender",
          "value": "MALE",
          "values": [ "MALE", "FEMALE", "OTHERS"]
  };
        
        $scope.chkdate=function (dob) {
            $scope.err='';
            var today=new Date();

            if(new Date(dob)>today)
            {
                $scope.err='Date of Birth should be less than today date';
                $scope.form.dob.$setValidity("dob", false);
            }
            else {
             var y = new Date(dob);
             $scope.age = Math.round((today - y)/(1000*60*60*24*365));
                $scope.form.dob.$setValidity("dob", true);
            }

        };

        $scope.clear=function()
        {
             $scope.firstname='';
             $scope.lastname='';
             $scope.age=0;
             $scope.dob='';
             $scope.gender='MALE';
             $scope.mobile=null;
			 $scope.comment='';
         };

        $scope.del=function(item) {
            $http.delete('/patients/api/patient/'+item.id+'/').then(
                $http.get('/patients/api/patient/?format=json')
                    .then(function(response){
						$scope.patients=response.data;
                    }));};

		$http.get('/patients/api/patient/?format=json').then(function(response){$scope.patients=response.data;});

        $scope.addp=function()
        {
            $http.get('/patients/api/patient/?format=json').then(function(response){$scope.patients=response.data;});

            var d=$filter('date')($scope.dob,'yyyy-MM-dd');

            $http.post('/patients/api/patient/?format=json', JSON.stringify({"id": $scope.id, "firstname":$scope.firstname,
               "lastname": $scope.lastname,
               "age": $scope.age, "dob": d,
               "gender": $scope.gender, "mobile": $scope.mobile, "comment": $scope.comment, "reg_date" :new Date()}),config);

             $scope.firstname='';
             $scope.lastname='';
             $scope.age=0;
             $scope.dob='';
             $scope.gender='MALE';
             $scope.mobile=null;
			 $scope.comment='';

        }
    });
