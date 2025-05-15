import React from "react";

function withAttribute(attributeName, attributeValue) {
  return (WrappedComponent) => (props) => {
    // Render your own <div> (or <span>) with the data-attribute…
    return React.createElement(
      "span",
      { [attributeName]: attributeValue },
      // …and nest the original component inside
      React.createElement(WrappedComponent, props)
    );
  };
}

export default function ouiaId(component_id) {
  return withAttribute("data-ouia-component-id", component_id)
}