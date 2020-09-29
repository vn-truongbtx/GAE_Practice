define([
    "dojo/_base/declare",
    "dojo/request",
    "dijit/_WidgetBase",
    "dijit/_OnDijitClickMixin",
    "dijit/_TemplatedMixin",
    "dijit/layout/ContentPane",
    "dojo/domReady!"
], function (declare, request, _WidgetBase, _OnClickDijitMixin, _TemplatedMixin, ContentPane) {

    return declare('ClassCreate', [_WidgetBase, _OnClickDijitMixin, _TemplatedMixin], {
        className: null,
        numberOfStudent: null,
        // language=HTML
        templateString: `
            <div id="createClassFS">
                <fieldset>
                    <div>
                        <label for="className">Class name: </label>
                        <input type="text"
                               data-dojo-observer="showValues"
                               data-dojo-attach-event="onChange: assignData"
                               data-dojo-attach-point="classNamePoint"
                               id="className"
                               name="class_name"
                        />
                    </div>
                    <div>
                        <label>Number of student: </label>
                        <input type="text"
                               data-dojo-attach-event="onChange: assignData"
                               data-dojo-attach-point="numberStudentPoint"
                               id="numberOfStudent"
                               name="number_of_student"
                        />
                    </div>
                    <button data-dojo-attach-event="click: createClass"
                            data-dojo-attach-point="createPoint">Create
                    </button>
                </fieldset>
            </div>
        `,
        id: "classContainer",
        title: "Class",
        assignData: function () {
            this.className = this.classNamePoint.value
            this.numberOfStudent = parseInt(this.numberStudentPoint.value)
        },
        createClass: function () {
            request.post('/api/class/', {
                data: JSON.stringify({
                    "name": this.className,
                    "number_of_student": this.numberOfStudent
                }),
                headers: {
                    "Content-Type": "application/json"
                }
            }).then((res) => {
                location.reload();
            })
        }
    });
});