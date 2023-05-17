var that;
class Tab {
  constructor(className) {
    // 导航主区域
    this.main = document.querySelector(className);
    // 获取到所有的标签页li
    this.liList = this.main.querySelectorAll(".li-item");
    this.liListActive = this.main.querySelectorAll(".li-item-active");
    // 获取到所有的子标签页li
    this.liChildList = this.main.querySelectorAll(".li-child-item");
    this.liChildListActive = this.main.querySelectorAll(
      ".li-child-item-active"
    );
    // 获取到所有的子标签页li
    this.liAirportList = this.main.querySelectorAll(".li-airport-item");
    this.liAirportListActive = this.main.querySelectorAll(
      ".li-airport-item-active"
    );
    that = this;
    // 绑定事件
    this.init();
  }

  init() {
    // 绑定标签页样式切换
    for (var i = 0; i < this.liList.length; i++) {
      this.liList[i].onclick = this.toggleSide;
    }
    for (var i = 0; i < this.liListActive.length; i++) {
      this.liListActive[i].onclick = this.toggleSide;
    }
    // 绑定子标签页样式切换
    for (var i = 0; i < this.liChildList.length; i++) {
      this.liChildList[i].onclick = this.toggleChildSide;
    }
    for (var i = 0; i < this.liChildListActive.length; i++) {
      this.liChildListActive[i].onclick = this.toggleChildSide;
    }
    for (var i = 0; i < this.liAirportList.length; i++) {
      this.liAirportList[i].onclick = this.toggleAirportSide;
    }
    for (var i = 0; i < this.liAirportListActive.length; i++) {
      this.liAirportListActive[i].onclick = this.toggleAirportSide;
    }
  }

  // 切换样式
  toggleSide() {
    // 清空当前所有选中的样式
    that.clearClass();
    this.className = "li-item-active";
    // 寻找当前选项卡的ID
    var panelId = "panel-" + this.id;
    // 将当前标签页对应的选项卡显示
    var panel = document.getElementById(panelId);
    panel.className = "panel-item-active";
  }

  // 清空所样式
  clearClass() {
    // 清空所有已经激活的样式
    var liActive = document.querySelectorAll(".li-item-active");
    for (var i = 0; i < liActive.length; i++) {
      liActive[i].className = "li-item";
    }
    // 将所有已经激活的选项卡清空
    var tabActive = document.querySelectorAll(".panel-item-active");
    for (var i = 0; i < tabActive.length; i++) {
      tabActive[i].className = "panel-item";
    }
  }

  // 切换样式
  toggleChildSide() {
    // 清空当前所有选中的样式
    that.clearChildClass();
    this.className = "li-child-item-active";
    // 寻找当前选项卡的ID
    var panelId = "panel-" + this.id;
    // 将当前标签页对应的选项卡显示
    var panel = document.getElementById(panelId);
    panel.className = "panel-child-item-active";
  }

  // 清空所样式
  clearChildClass() {
    // 清空所有已经激活的样式
    var liActive = document.querySelectorAll(".li-child-item-active");
    for (var i = 0; i < liActive.length; i++) {
      liActive[i].className = "li-child-item";
    }
    // 将所有已经激活的选项卡清空
    var tabActive = document.querySelectorAll(".panel-child-item-active");
    for (var i = 0; i < tabActive.length; i++) {
      tabActive[i].className = "panel-child-item";
    }
  }

  // 切换样式
  toggleAirportSide() {
    // 清空当前所有选中的样式
    that.clearAirportClass();
    this.className = "li-airport-item-active";
    // 寻找当前选项卡的ID
    var panelId = "panel-" + this.id;
    // 将当前标签页对应的选项卡显示
    var panel = document.getElementById(panelId);
    panel.className = "panel-airport-item-active";
  }

  // 清空所样式
  clearAirportClass() {
    // 清空所有已经激活的样式
    var liActive = document.querySelectorAll(".li-airport-item-active");
    for (var i = 0; i < liActive.length; i++) {
      liActive[i].className = "li-airport-item";
    }
    // 将所有已经激活的选项卡清空
    var tabActive = document.querySelectorAll(".panel-airport-item-active");
    for (var i = 0; i < tabActive.length; i++) {
      tabActive[i].className = "panel-airport-item";
    }
  }
}

var tab = new Tab(".page-right");
