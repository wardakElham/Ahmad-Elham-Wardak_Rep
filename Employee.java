package Q1;
public class Employee {
    private int EmpId;
    private String EmpName;
    private double EmpSalary;
    private double EmpBonus;
    private double EmpTotalPay;

    public Employee(int EmpId, String EmpName, double EmpSalary, double EmpBonus, double EmpTotalPay) {
        this.EmpId = EmpId;
        this.EmpName = EmpName;
        this.EmpSalary = EmpSalary;
        this.EmpBonus = EmpBonus;
        this.EmpTotalPay = EmpTotalPay;
    }
    public int getEmpId(){
        return EmpId;
    }
    public void setEmpId(int EmpId){
        this.EmpId = EmpId;
    }
    public String getEmpName(){
        return EmpName;
    }
    public void setEmpName(String EmpName){
        this.EmpName = EmpName;
    }
    public double getEmpSalary(){
        return EmpSalary;
    }
    public void setEmpSalary(double EmpSalary){
        this.EmpSalary = EmpSalary;
    }
    public double getEmpBonus(){
        return EmpBonus;
    }
    public void setEmpBonus(double EmpBonus){
        this.EmpBonus = EmpBonus;
    }
    public double getEmpTotalPay(){
        return EmpTotalPay;
    }
    public void setEmpTotalPay(double EmpTotalPay){
        this.EmpTotalPay = EmpTotalPay;
    }
    public void prints(){
        System.out.println(EmpId + EmpName + EmpSalary + EmpBonus + EmpTotalPay);
    }
}