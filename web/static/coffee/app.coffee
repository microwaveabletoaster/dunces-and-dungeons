$(document).ready(
  ()->
    console.log 'nicela!'
    source = new EventSource '/stream'
    source.onmessage = (event)->
      $('#main').append event.data
      # if make_choice was called
      if event.data[0..5] == 'CHOICE'
        console.log "CREATING A FORM"
        make_form(event)
        # choices should be divided with a |
)

make_form = (event) ->
  options = event.data[6..].split '|'
  form = "<form id=\"ch\" action=\"/choice\" method='post'>"
  for a in options
    form += "<input type=\"radio\" name='makechoice' value=\"#{a}\">#{a}<br>"
  form += "<input type=\"submit\" value=\"choose!\">"
  form += "</form>"
  $('#main').append(form)



random = () ->
  console.log 'this is a random-ass method to hopefully stop chrome frmo caching this javascript, lulz'
