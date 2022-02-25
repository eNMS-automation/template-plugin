import {
  call,
  configureForm,
  configureNamespace,
  notify,
  openPanel,
} from "/static/js/version/base.js";

function autofillForm() {
  $("#custom-ip_address").val("192.168.155.1");
  $("#custom-carry_customer_traffic").prop("checked", true);
  notify("Values filled programatically in JavaScript.", "success", 5);
}

function resetForm() {
  $("[id^='custom-']").val("").prop("checked", false);
  notify("Values resetted programatically in JavaScript.", "success", 5);
}

function submitForm() {
  call({
    url: "/process_form_data",
    form: "custom-form",
    callback: function (ipAddress) {
      $("#custom-ip_address").val(ipAddress);
      notify("Form successfully submitted.", "success", 5, true);
    },
  });
}

function showFormPanel() {
  openPanel({
    name: "panel",
    title: "Form in a Panel",
    size: "600 auto",
  });
}

function submitPanelForm() {
  notify("Form submitted.", "success", 5);
  $("#panel").remove();
}

$(document).ready(function () {
  configureForm("custom");
});

configureNamespace("plugins", [
  autofillForm,
  resetForm,
  showFormPanel,
  submitForm,
  submitPanelForm,
]);
